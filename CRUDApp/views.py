from itertools import count

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, models
from django.http import HttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
from .models import Contact
from django.contrib.auth.decorators import login_required


# Create your views here.

def get_request(request):
    employees=Employee.objects.all()
    return render(request,"crudapp/alldetails.html",context={"employees":employees})

def post_request(request):
    if request.method=="POST":
        post= EmployeeForm(request.POST)
        if post.is_valid():
            post.save()
            # return HttpResponse("<h1>Successfully Registered <a href='/crud/get'>Click Here</a>to navigate all employee</h1>")
            return redirect('/crud/get')
    form=EmployeeForm()
    return render(request,"crudapp/create.html",context={"form":form})

def delete_employee(request,id):
    emp=Employee.objects.get(id=id)

    emp.delete()
    return redirect('/crud/get')


def update_employee(request,id):
    # emp=Employee.objects.get(id=id)
    emp = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        put=EmployeeForm(request.POST,instance=emp)
        if put.is_valid():
            put.save()
            return redirect('/crud/get')
    return render(request,"crudapp/update.html",context={"emp":emp})

def search_employee(request):
    srch=request.GET.get("search")

    if srch:
        # emp_name=Employee.objects.filter(name__icontains=srch)
        # emp_id=Employee.objects.filter(empid__icontains=srch)
        # emp_ph=Employee.objects.filter(phonenumber__icontains=srch)
        # employees=emp_name.union(emp_id,emp_ph)
        employees=Employee.objects.filter(Q(name__icontains=srch) | Q(empid__icontains=srch) | Q(phonenumber__icontains=srch) )
        count=employees.count()


    else:
        employees= Employee.objects.all()
        count=employees.count()

    return render(request,"crudapp/alldetails.html",context={"employees":employees,"count":count})


def login_user(request):
    page="login"
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        try:
             User.objects.get(username=username)
        except:
             messages.error(request,"Invalid username")

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('/crud/get')


    return render(request,"crudapp/login_and_register.html",context={"page":page})


@login_required
def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(user=request.user).filter(
            models.Q(name__icontains=query) | models.Q(phone__icontains=query)
        )
    else:
        contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact/contact_list', {'contact': contacts})

@login_required
def contact_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        Contact.objects.create(user=request.user, name=name, phone=phone, email=email, address=address)
        return redirect('contact_list')
    return render(request, 'contact/contact_form.html')

@login_required
def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.phone = request.POST['phone']
        contact.email = request.POST.get('email', '')
        contact.address = request.POST.get('address', '')
        contact.save()
        return redirect('contact_list')
    return render(request, 'contact/contact_form.html', {'contact': contact})

@login_required
def contact_delete(request, pk):
        contact = Contact.objects.get(pk=pk, user=request.user)
        contact.delete()
        return redirect('contact_list')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contact_list')
    else:
        form = UserCreationForm()
    return render(request, 'contact/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('contact_list')
    else:
        form = AuthenticationForm()
    return render(request, 'contact/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


