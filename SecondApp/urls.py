from django.urls import path
from SecondApp import views


urlpatterns=[
    path('sample/',views.secondappfun),
    path('ipl/',views.ipltable),
    path('product/',views.productlist),
    path('total/',views.totalprice)
]















