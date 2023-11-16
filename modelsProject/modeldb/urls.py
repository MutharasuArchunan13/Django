from django.urls import path
from .views import model_proj 
urlpatterns = [
    path('',model_proj,name='model_proj'),
]

