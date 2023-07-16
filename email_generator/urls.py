
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^send_email/', views.send_email, name='send_email'),
    url(r'^track-email/', views.track_email, name='track_email'),
    url(r'^get-results/', views.get_results, name='get-result'),

]