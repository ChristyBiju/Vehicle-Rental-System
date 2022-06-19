from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("",views.index, name = 'home'),
    # path("",views.register,name='register'),
    path("home",views.index, name = 'home'),
    path("about",views.about,name = 'about'),
    path("contact",views.contact,name = 'contact'),
    path("vehicles",views.Order,name = 'vehicles'),
    path("bike",views.bike,name = 'bike'),
    path("bus",views.bus,name = 'bus'),
    path("register", views.register, name="register"),
    path("login", views.login_request, name="login"),
    path("bill", views.bill, name="bill"),

    ]

