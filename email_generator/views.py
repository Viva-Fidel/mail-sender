# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.db.models import Count, Sum, Case, When, IntegerField
from django.utils import timezone
from django.template import Template, Context
from subscribers.models import Subscriber
from django.shortcuts import redirect
from .models import Report
from django.http import JsonResponse

from mail_sender.config import *
from tasks import send_scheduled_emails

import datetime
import uuid
from datetime import timedelta


def get_results(request):
    """
    Получение результатов по отправленным письмам в формате JSON.
    """
    if request.method == 'GET':
        sent_emails_data = Report.objects.values('date_of_mailing').annotate(
            sent_emails=Count('pk'),
            opened_emails=Sum(Case(When(is_opened=True, then=1), default=0, output_field=IntegerField()))
        ).order_by('-date_of_mailing')

        # Преобразование QuerySet в список словарей
        results_list = list(sent_emails_data)

        # Возвращение JSON-ответа
        return JsonResponse(results_list, safe=False)


def track_email(request):
    """
    Обработка запроса для отслеживания открытия письма.
    """
    if 'tracking_id' in request.GET:
        tracking_id = request.GET.get('tracking_id')
        report = Report.objects.get(tracking_id=tracking_id)
        report.is_opened = True
        report.save()
    return redirect('home')


def send_email(request):
    """
    Обработка запроса на отправку письма.
    """
    if request.method == 'POST':
        email_title = request.POST.get('email_title')
        html_data = request.POST.get('html_data')
        email_time = request.POST.get('email_time')
        email_date = request.POST.get('email_date')

        if email_time != '' and email_date != '':
            email_datetime = datetime.datetime.strptime(email_date + ' ' + email_time, '%Y-%m-%d %H:%M')
            current_datetime = timezone.now()

            # Проверка, что email_datetime находится в будущем
            if email_datetime > current_datetime:
                email_datetime_adjusted = email_datetime - timedelta(hours=3)

                # Запланировать задачу на указанную дату и время
                send_scheduled_emails.apply_async(
                    args=(email_title, html_data),
                    eta=email_datetime_adjusted,
                )
                return JsonResponse({'success': True})  # Вернуть JSON-ответ об успехе
            else:
                return JsonResponse({'success': False})  # Вернуть JSON-ответ о неудаче

        elif email_time == '' and email_date == '':
            # Получение всех подписчиков из базы данных
            subscribers = Subscriber.objects.all()
            date_of_mailing = timezone.now()

            for subscriber in subscribers:
                # Генерация персонализированного содержимого письма
                first_name = subscriber.first_name
                last_name = subscriber.last_name
                date_of_birth = subscriber.date_of_birth
                email = subscriber.email

                report = Report.objects.create(
                    email=subscriber,
                    date_of_mailing=date_of_mailing,
                    is_opened=False,
                )
                # Генерация уникального идентификатора для созданного экземпляра отчета
                report.tracking_id = uuid.uuid4()
                report.save()

                # Генерация персонализированного содержимого письма
                template = Template(html_data)
                context = Context({
                    'first_name': first_name,
                    'last_name': last_name,
                    'date_of_birth': date_of_birth,
                })
                html_data_personalized = template.render(context)
                html_data_personalized += '<img src="http://127.0.0.1:8000/track-email/?tracking_id={}" alt="Email Tracking Pixel" width="1" height="1" style="display:none;">'.format(str(report.tracking_id))
                html_data_personalized += '<br><a href="http://127.0.0.1:8000/track-email/?tracking_id={}">Перейдите на сайт</a>'.format(str(report.tracking_id))

                # Отправка персонализированного письма
                send_mail(
                    email_title,
                    '',
                    EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                    html_message=html_data_personalized,
                )

            return JsonResponse({'success': True})  # Вернуть JSON-ответ об успехе

        else:
            return JsonResponse({'success': False})  # Вернуть JSON-ответ о неудаче