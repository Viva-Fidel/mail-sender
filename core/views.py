# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from subscribers.forms import SubscriberForm

# Create your views here.
def index (request):
    form = SubscriberForm()
    return render (request, 'core/index.html', {'form': form})
