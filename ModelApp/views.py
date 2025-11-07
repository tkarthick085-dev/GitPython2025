from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def getemployeedata(request):
    employees=Employee.objects.all()  # to retrieve all the datas from database table

    return render(request,"modelapp/AllEmployees.html",context={"employees":employees})


def create_employee(request):
    if request.method == "POST":
        if(  request.POST.get("empid") and request.POST.get("name") and request.POST.get("phno")
           and request.POST.get("email") and request.POST.get("address")):
           emp=Employee()
           emp.empid=request.POST.get("empid")
           emp.name=request.POST.get("name")
           emp.phno=request.POST.get("phno")
           emp.email=request.POST.get("email")
           emp.address=request.POST.get("address")
           emp.save()
           return HttpResponse("Successfully Registered")

    forms=EmployeeForm()
    return render(request,"modelapp/employeeform.html",context={"forms":forms})
















