from django.db import models

# Create your models here.
class lab(models.Model):
    lab_id =models.IntegerField() 
    lab_name= models.CharField(max_length=30)
    lab_address = models.CharField(max_length=50)

    def __str__(self):
      return f"name:{self.lab_name},address:{self.lab_address},id:{self.lab_id}"
