from django import forms

class students(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    id = forms.IntegerField()