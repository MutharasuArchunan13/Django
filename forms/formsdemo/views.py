
# Create your views here.
from django.shortcuts import render
from . import forms
def form_return(request):
    form = forms.students
    return render(request,'formsdemo/forms.html',context={'form':form})