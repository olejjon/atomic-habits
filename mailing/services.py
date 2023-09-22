import logging
from datetime import timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from mailing.mailing_log_models import MailingLog
from mailing.mailing_models import Mailing

logger = logging.getLogger(__name__)


def send_email(mailing, client):
    try:
        send_mail(
            subject=mailing.title,
            message=mailing.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email],
            fail_silently=False
        )
        MailingLog.objects.create(
            mailing=mailing,
            attempt_status=MailingLog.AttemptStatus.SUCCESSFULLY,
        )
    except Exception as e:
        MailingLog.objects.create(
            mailing=mailing,
            attempt_status=MailingLog.AttemptStatus.NOT_SUCCESSFULLY,
            server_response=str(e)
        )


def calculate_next_send_time(frequency, last_send_time):
    if frequency == Mailing.Frequency.DAILY:
        return last_send_time + timedelta(days=1)
    elif frequency == Mailing.Frequency.WEEKLY:
        return last_send_time + timedelta(weeks=1)
    elif frequency == Mailing.Frequency.MONTHLY:
        return last_send_time + timedelta(days=30)


def process_pending_mailings():

    now = timezone.now() + timedelta(hours=3)
    logger.info("Processing")
    pending_mailings = Mailing.objects.all()

    for mailing in pending_mailings:
        print(mailing)
        next_send_time = calculate_next_send_time(mailing.frequency, mailing.mailing_time)

        match mailing.status:

            case Mailing.Status.CREATED:
                if mailing.mailing_time <= now:
                    clients = mailing.clients.all()
                    for client in clients:
                        send_email(mailing, client)
                    mailing.status = Mailing.Status.STARTED
                    mailing.mailing_time = next_send_time
                    mailing.save()

            case Mailing.Status.STARTED:
                if mailing.mailing_time <= now:
                    clients = mailing.clients.all()
                    for client in clients:
                        send_email(mailing, client)
                    mailing.mailing_time = next_send_time
                    mailing.save()