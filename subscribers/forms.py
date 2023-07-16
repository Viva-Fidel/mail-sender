# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone
from django.core.validators import EmailValidator

# Форма добавления нового подписчика на сайте
class SubscriberForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'subscriber-first-name', 'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'subscriber-last-name', 'placeholder': 'Фамилия'}))
    date_of_birth = forms.DateField(label='Дата рождения', widget=forms.TextInput(attrs={'class': 'form-control', 'id':'subscriber-date-of-birth', 'placeholder': 'Дата рождения'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'id':'subscriber-email', 'placeholder': 'Почта'}), validators=[EmailValidator()])

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        today = timezone.now().date()
        # Проверяем, что дата рождения не в будущем или сегодняшнем дне
        if date_of_birth >= today:
            raise forms.ValidationError("Пожалуйста выберите корректную дату")

        return date_of_birth
