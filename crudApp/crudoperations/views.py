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

def delete_student(request,id):
    stud = student.objects.get(id = id)
    stud.delete()
    return redirect('/check')
def update_student(request,id):
    stud = student.objects.get(id = id)
    form = studentForm(request.POST,instance = stud)
 
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request,'crudoperations/update.html',{'stud':stud})
