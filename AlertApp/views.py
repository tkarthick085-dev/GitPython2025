from django.contrib import messages
from django.shortcuts import render
from django.template.context_processors import request


# Create your views here.

def alertmessage(request):
    return render(request,"alertapp/alerts.html")

def info_message(request):
    messages.info(request, "It is informational message")
    return render(request, "alertapp/alerts.html")

def success_message(request):
    messages.success(request,"It is Success message")
    return render(request, "alertapp/alerts.html")

def warning_message(request):
    messages.warning(request,"It is Warning message")
    return render(request, "alertapp/alerts.html")

def error_message(request):
    messages.error(request,"It is Error message")
    return render(request, "alertapp/alerts.html")