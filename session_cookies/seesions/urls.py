from django.urls import path
from . import views
urlpatterns = [
    path('',views.count_sessions,name='count_sessions'),
]
