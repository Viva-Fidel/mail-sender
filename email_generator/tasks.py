# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.utils import timezone
from django.template import Template, Context
from subscribers.models import Subscriber
from .models import Report

from celery import shared_task
from mail_sender.config import *
import uuid


@shared_task
def send_personalized_email(email_title, html_data, first_name, last_name, date_of_birth, email, report_id):
    """
    Функция для отправки персонализированного письма подписчику
    """

    # Генерация персонализированного содержимого письма
    template = Template(html_data)
    context = Context({
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
    })
    html_data_personalized = template.render(context)
    html_data_personalized += '<img src="http://127.0.0.1:8000/track-email/?tracking_id={}" alt="Email Tracking Pixel" width="1" height="1" style="display:none;">'.format(report_id)
    html_data_personalized += '<br><a href="http://127.0.0.1:8000/track-email/?tracking_id={}">Перейдите на сайт</a>'.format(report_id)

    # Отправка персонализированного письма
    send_mail(
        email_title,
        '',
        EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        html_message=html_data_personalized,
    )


@shared_task
def send_scheduled_emails(email_title, html_data):
    """
    Функция для отправки запланированных писем подписчикам
    """

    # Получение всех подписчиков из базы данных
    subscribers = Subscriber.objects.all()
    date_of_mailing = timezone.now()

    for subscriber in subscribers:
        first_name = subscriber.first_name
        last_name = subscriber.last_name
        date_of_birth = subscriber.date_of_birth
        email = subscriber.email

        # Генерация персонализированного содержимого письма
        report = Report.objects.create(
            email=subscriber,
            date_of_mailing=date_of_mailing,
            is_opened=False,
        )
        # Генерация уникального идентификатора для созданного экземпляра отчета
        report.tracking_id = uuid.uuid4()
        report.save()

        report_id = str(report.tracking_id)

        send_personalized_email.delay(email_title, html_data, first_name, last_name, date_of_birth, email, report_id)
