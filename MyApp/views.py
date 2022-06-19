# from curses.ascii import US
import email
from email import message
from tkinter import N
from unicodedata import name
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User,auth
from .forms import NewUserForm
from .models import Cars,Order,Customer,Contact


def index(request):
	return render(request,'index.html')


def about(request):
    return render(request,'about.html ')

def contact(request):
	if request.method == "POST":
		name = request.POST.get('name','')
		email = request.POST.get('email','')
		num = request.POST.get('num','')
		message = request.POST.get('message','')
		contact = Contact(name=name,email=email,num=num,message=message)
		contact.save()
	return render(request,'contact.html')


def vehicles(request):
	cars = Cars.objects.all()
	print(cars)
	# params = {'cars' : cars}
	return render(request,'cars.html',{'cars':cars})


def bike(request):
    return render(request,'bike.html')

def bus(request):
    return render(request,'bus.html')


def register_request(request):
	if request.method == "POST":
		r_username = request.POST['r_username']
		r_name = request.POST['r_name']
		r_number = request.POST['r_number']
		r_email = request.POST['r_email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		myuser = User.objects.create_user(r_username=r_username,r_mail=r_email,password1=password1)

		myuser.save()
		messages.success(request,"You are successfully signed in!")
		return redirect('/')

	return render(request,'register.html')

def register(request):
	if request.method == "POST":
		name = request.POST['name']
		username = request.POST['username']
		number = request.POST['number']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		user = User.objects.create_user(username=username,password1=password1,email=email,name=name,number=number)
		user.save()
		print("user created")
		return redirect('/')

	else:
		print("error")
		return render(request,'register.html')

def customer(request):
	if request.method == "POST":
		r_username = request.POST.get('r_username')
		r_name = request.POST.get('r_name')
		r_number = request.POST.get('r_number')
		r_email = request.POST.get('r_email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')

		customer = Customer(r_username=r_username,r_name=r_name,r_mail=r_email)
		customer.save()
	return render(request,'register.html')


def login_request(request):
	return render(request,'login.html')

def bill(request):
    return render(request,'bill.html')

def Order(request):
	if request.method =="POST":
		car = request.POST.get('car','')
		days = request.POST.get('days','')

		contact = Order(car=car,days=days)
		contact.save()
	return render(request,"cars.html")

