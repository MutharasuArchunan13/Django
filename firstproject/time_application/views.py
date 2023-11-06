from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time(request):
    ret_time='The current time: {}'.format(datetime.datetime.now())
    return HttpResponse(ret_time)