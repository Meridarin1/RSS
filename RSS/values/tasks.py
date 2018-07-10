from celery.task.schedules import crontab
from celery.decorators import periodic_task
from .scraper import *


@periodic_task(run_every=(crontab(hour='12')), name="checking_RSS", ignore_result=True)
def scraper():
    scrape()