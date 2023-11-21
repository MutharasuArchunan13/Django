from django import forms
from crudoperations.models import student

class studentForm(forms.ModelForm):
    class Meta:
        model = student #this is predefined that Meta data have data about models
        fields = '__all__'
        #if you want to change the name of the fields use exclude =['field_name]