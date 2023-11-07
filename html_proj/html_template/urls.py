from django.contrib import admin
from django.urls import path, include


from html_template import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/',views.temp)
]