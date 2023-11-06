from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def show(request):
    message = '<h1>Hey buddy welcome my first application</h1>'
    return HttpResponse(message)
