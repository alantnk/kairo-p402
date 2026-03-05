import os

from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery("config")
app.conf.broker_url = config("CELERY_BROKER_URL", default="redis://localhost:6379/0")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
