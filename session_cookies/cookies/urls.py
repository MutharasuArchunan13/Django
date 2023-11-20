from django.urls import path
from . import views
urlpatterns = [
    path('',views.cookies_count,name='cookies_count'),
]
