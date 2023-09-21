from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.core.management import BaseCommand

from mailing.services import process_pending_mailings
import logging
from django.conf import settings

logger = logging.getLogger(__name__)


def start_scheduler():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)

    scheduler.add_job(
        process_pending_mailings,
        trigger=IntervalTrigger(minutes=1),
        id="process_pending_mailings",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'my_job'.")

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler shut down successfully!")


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_scheduler()
