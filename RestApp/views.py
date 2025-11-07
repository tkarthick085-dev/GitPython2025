from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Employee
from .serializer import UserSerializer
from django.contrib.auth import views



# Create your views here.

@api_view(['GET'])
def get_request(request):
    employees=Employee.objects.all()
    serial=UserSerializer(employees)
    return Response(serial.data)