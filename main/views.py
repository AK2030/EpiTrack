from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
import re

# Create your views here.

# Landing page
def map(request):
	return render(request=request, template_name="main/map.html")

@login_required(login_url='/')
def hospital(request):
	return render(request=request, template_name="main/hospital.html")

# Home page
@login_required(login_url='/')
def home(request):
	return render(request=request,
		          template_name="main/home.html")

# Signed in as guest
def guest_home(request):
	return render(request=request,
		          template_name="main/guest_home.html")

# Covid-19
@login_required(login_url='/')
def covid19(request):
	return render(request=request, template_name="main/covid19.html")

# Foodborne
@login_required(login_url='/')
def foodborne(request):
	return render(request=request, template_name="main/foodborne.html")

# Airborne
@login_required(login_url='/')
def airborne(request):
	return render(request=request, template_name="main/airborne.html")

# Profile
@login_required(login_url='/')
def profile(request):
	return render(request=request, 
				  template_name="main/profile.html")

# Edit Profile
@login_required(login_url='/')
def edit_profile(request):
	if request.method == "POST":
		form = CreateChangeForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect("main:profile")

	form = CreateChangeForm(instance=request.user)
	return render(request, "main/edit_profile.html", context={"form":form})

# Login page
def login(request):
	return render(request=request,
		          template_name="main/login.html")

# Account is created
@login_required(login_url='/')
def created(request):
	return render(request=request,
		          template_name="main/accountcreated.html")

# Register Page
def register(request):
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect("main:accountcreated")

		else:
			password1 = form.cleaned_data.get('password1')
			password2 = form.cleaned_data.get('password2')
			username = form.cleaned_data.get('username')
			# username validation is not working
			# password validation (checking if the passwords are the same is not working either)
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username is already taken.')
			if password1 != password2:
				messages.info(request, 'Your passwords do not match')
			if len(password1) < 8:
				messages.info(request, 'Password must be at least 8 characters long.')
			if not re.findall('\d', password1):
				messages.info(request, 'Password must contain one numeric value.')
			if not re.findall('[a-z]', password1):
				messages.info(request, 'Password must contain at least one lowercase value.')
			if not re.findall('[A-Z]', password1):
				messages.info(request, 'Password must contain at least one uppercase value.')
			if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password1):
				messages.info(request, 'Password must contain at least one symbol.')
			if password1.isdigit():
				messages.info(request, 'The password may not be entirely numeric.')


	form = CreateUserForm
	return render(request, "main/register.html", context={"form":form})

# In order to login to account
def loginpage(request):
	
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				auth.login(request, user)
				return redirect("main:home")

			else:
				messages.info(request, 'Username or Password is incorrect.')

		context = {}
		return render(request, "main/login.html", context)

# Logout
@login_required(login_url='/')
def logoutpage(request):
	logout(request)
	return redirect("main:login")
