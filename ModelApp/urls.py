from django.urls import path

from ModelApp import views

urlpatterns=[
    path('get/',views.getemployeedata),
    path('create',views.create_employee)
]