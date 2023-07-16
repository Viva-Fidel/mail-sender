from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^save_subscriber/', views.save_subscriber, name='save_subscriber'),
]