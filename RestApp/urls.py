from django.urls import path

from RestApp import views





urlpatterns=[
    path('get/',views.get_request)
]