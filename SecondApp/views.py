import datetime
from http.client import HTTPResponse

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def secondappfun(request):
    return HttpResponse("This is a second app")

def ipltable(request):
    cmp="PEPSI"
    date=datetime.datetime.now()
    return render(request,"secondapp\ipltable.html",context={"name":cmp,"date":date})

def productlist(request):
    return render(request,"secondapp\products.html")

def totalprice(request):
    mobiles= int(request.GET.get("mobiles"))
    laptop = int(request.GET.get("laptop"))
    keyboard = int(request.GET.get("keyboard"))
    tablet = int(request.GET.get("tablet"))
    harddisk = int(request.GET.get("harddisk"))
    total=mobiles+laptop+keyboard+tablet+harddisk
    return render(request,r"secondapp\totalprice.html",context={"total":total})