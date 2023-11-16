from django.shortcuts import render
from .models import lab
#models business logic
def model_proj(request):
    # now we learning model so imort the details from database
    model_values = lab.objects.all().values('lab_id','lab_name','lab_address')
    list_data ={'data':model_values}
    return render (request,'modeldb/model.html',context=list_data)