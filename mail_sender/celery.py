# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from celery import Celery
import os

# Установка модуля Django для настроек по умолчанию для программы 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mail_sender.settings')

app = Celery('mail_sender')

# Загрузка настроек из объекта settings модуля django.conf
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузка задач из всех зарегистрированных приложений
app.autodiscover_tasks()