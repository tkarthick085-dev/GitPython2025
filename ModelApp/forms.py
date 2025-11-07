from django import forms

class EmployeeForm(forms.Form):
    empid=forms.IntegerField()
    name=forms.CharField(max_length=20)
    phno=forms.IntegerField()
    email=forms.CharField(max_length=64)
    address=forms.CharField(max_length=200)