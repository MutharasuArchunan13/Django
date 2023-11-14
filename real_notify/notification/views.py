from django.shortcuts import render,redirect

# Create your views here.

from .models import Task
from .tasks import process_field

def upload_file(request):
    if request.method == 'POST':
       file =request.FILES['file']
       task = Task.objects.create(file = file)
       process_field.apply_asyc(args =[task.id])  #start celery task
       return redirect(request,'status')
    return render(request , 'upload.html')
def task_status (request):
    tasks = Task.objects.all()
    return render(request,'staus.html',{'tasks':tasks})