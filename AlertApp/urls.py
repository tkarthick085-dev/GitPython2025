from django.contrib import admin
from django.urls import path, include
from AlertApp import views as alert_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', alert_views.sample),
    path('', alert_views.homepage),
    path('login/', alert_views.loginpage),
    path('register/', alert_views.registerpage),
    path('payment/', alert_views.paymentpage),

    path('second/', include("SecondApp.urls")),
    path('model/', include("ModelApp.urls")),
    path('multi/', include("Multimodel.urls")),
    path('alert/', include("AlertApp.urls")),
    path('crud/', include("CRUDApp.urls")),
    path('api-auth/', include("rest_framework.urls")),
]
