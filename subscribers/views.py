# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.shortcuts import render
from subscribers.forms import SubscriberForm
from subscribers.models import Subscriber

def save_subscriber(request):
    """
    Функция для сохранения подписчика в базе данных
    """

    if request.method == 'POST':
        form = SubscriberForm(request.POST)

        if form.is_valid():
            # Создание нового объекта Subscriber и сохранение его в базе данных
            subscriber = Subscriber(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                email=form.cleaned_data['email']
            )
            subscriber.save()
            return JsonResponse({'success': True})
        else:
            # Если форма недействительна, возвращаем ошибки в формате JSON
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = SubscriberForm()

    return render(request, 'core/index.html', {'form': form})
