from django.http import HttpResponse
from django.shortcuts import render

from sam_notify.celery import app

def push_messages_to_celery(request):
    messages = ["the file read successfully", "notification pussed", "notification pushed successfully"]
    for message in messages:
        app.send_task("sam_notify.celery.send_message", args=[message])
    return HttpResponse("Messages pushed to Celery")


