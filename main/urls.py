"""OutbreakTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views

app_name = "main"

urlpatterns = [

    path("map/", views.map, name="map"),

    path("hospital/", views.hospital, name = "hospital"),

    path("home/", views.home, name = "home"),

    path("guest_home/", views.guest_home, name = "guest_home"),

    path("covid19/", views.covid19,name = "covid19"),

    path("foodborne/", views.foodborne,name = "foodborne"),

    path("airborne/", views.airborne,name = "airborne"),

    path("register/", views.register, name = "register"),

    path("accountcreated/", views.created, name = "accountcreated"),

    path("", views.loginpage, name = "login"),

    path("logout/", views.logoutpage, name = "logout"),

    path("profile/", views.profile, name = "profile"),

    path("edit_profile/", views.edit_profile, name = "edit_profile"),

    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name="main/password_reset.html"),
    name="reset_password"),

    path('web/password_reset/done/', 
    auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"), 
    name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="main/password_reset_form.html"), 
    name="password_reset_confirm"),

    path('web/reset/done/', 
    auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"), 
    name="password_reset_complete"),
    
]