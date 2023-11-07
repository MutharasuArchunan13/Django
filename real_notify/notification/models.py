from django.db import models

# Create your models here.
class Task(models.Model):
    file= models.FileField(upload_to='uploads/')
    status = models.CharField(max_length=20,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)