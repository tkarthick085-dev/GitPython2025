from django.contrib import admin
from django.urls import path, include
from MyFirstDjangoProject import views as v1  # assuming your views are here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', v1.sample),
    path('', v1.homepage),
    path('login/', v1.loginpage),
    path('register/', v1.registerpage),
    path('payment/', v1.paymentpage),
    path('second/', include("SecondApp.urls")),
    path('model/', include("ModelApp.urls")),
    path('multi/', include("Multimodel.urls")),
    path('alert/', include("AlertApp.urls")),
    path('crud/', include("CRUDApp.urls")),
    path('api-auth/', include("rest_framework.urls")),
]
