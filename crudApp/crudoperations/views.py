from django.shortcuts import render,redirect
from crudoperations.models import student
from crudoperations.forms import studentForm

# Create your views here.
def studtent_retrive(request):
    students = student.objects.all()
    return render(request,'crudoperations/crudoperation.html',{'student':students})

#receive the data from user to store db
def add_student(request):
    form = studentForm()
    if request.method == 'POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudoperations/forms.html',{"form":form})