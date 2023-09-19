from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from mailing.mailing_models import Mailing
from mailing.services import send_email

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


def calculate_next_send_time(frequency, last_send_time):
    if frequency == Mailing.Frequency.DAILY:
        return last_send_time + timedelta(days=1)
    elif frequency == Mailing.Frequency.WEEKLY:
        return last_send_time + timedelta(weeks=1)
    elif frequency == Mailing.Frequency.MONTHLY:
        return last_send_time + timedelta(days=30)


def process_pending_mailings():
    now = datetime.now()
    pending_mailings = Mailing.objects.filter(
        mailing_time__lte=now,
        status=Mailing.Status.CREATED
    )

    for mailing in pending_mailings:
        next_send_time = calculate_next_send_time(mailing.frequency, mailing.mailing_time)
        if next_send_time <= now:
            mailing.status = Mailing.Status.STARTED
            mailing.save()
            clients = mailing.clients.all()
            for client in clients:
                send_email(mailing, client)
                # Создать запись в логах

            mailing.mailing_time = next_send_time
            mailing.status = Mailing.Status.CREATED
            mailing.save()


scheduler.add_job(process_pending_mailings, trigger="interval", minutes=1)
print("Scheduler is starting...")
scheduler.start()