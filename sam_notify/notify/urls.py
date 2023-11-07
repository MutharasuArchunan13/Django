# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Add your URL pattern here
    path('push-messages/', views.push_messages_to_celery, name='push_messages'),
]
