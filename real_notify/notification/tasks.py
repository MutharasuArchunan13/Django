from celery import shared_task
from .models import Task
from .consumers import Publisher

@shared_task
def process_field(task_id):
    task = Task.objects.get(pk=task_id)
    task.status ='Processing'
    task.save()

    #simulate file processing
    import time
    time.sleep(5)

    task.status='completed'
    task.save()
    
    #notify the websocket clints
    
    Publisher.publish_task_status(task_id)
