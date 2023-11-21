from django.contrib import admin
from .models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ['name','roll','sid']
admin.site.register(student,studentAdmin)