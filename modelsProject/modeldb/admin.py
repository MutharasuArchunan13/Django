from django.contrib import admin
from modeldb.models import lab
# Register your models here.
class lab_admin(admin.ModelAdmin):
    list_display = ('lab_id','lab_name','lab_address')
    
admin.site.register(lab,lab_admin)
