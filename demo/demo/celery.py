import os
from celery import Celery
from django.conf import settings


DJANGO_SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if not DJANGO_SETTINGS_MODULE:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings.dev')


app = Celery('demo')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
