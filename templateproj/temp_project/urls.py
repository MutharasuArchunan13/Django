from django.urls import path
from . import views

urlpatterns = [
    # Add your URL pattern here
    path('temp/', views.html_file_rendering, name='html_render'),
]
