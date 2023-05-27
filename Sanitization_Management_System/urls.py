"""Sanitization_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from sanitization.views import *
from django.conf import settings
from django.conf.urls.static import static
from app1 import views
from sanitization import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('services', services, name='services'),
    path('servicereq/<int:pid>', servicereq, name='servicereq'),
    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('add_Service', add_Service, name='add_Service'),
    path('editService/<int:pid>', editService, name='editService'),
    path('deleteService/<int:pid>', deleteService, name='deleteService'),
    path('newRequest', newRequest, name='newRequest'),
    path('onthewayReq', onthewayReq, name='onthewayReq'),
    path('inprocessReq', inprocessReq, name='inprocessReq'),
    path('rejectReq', rejectReq, name='rejectReq'),
    path('completeReq', completeReq, name='completeReq'),
    path('allReq', allReq, name='allReq'),
    path('deleteReq/<int:pid>', deleteReq, name='deleteReq'),
    path('request_details/<int:pid>', request_details, name='request_details'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout'),
    path('track', track, name='track'),
    path('bwdateReport', bwdateReport, name='bwdateReport'),
    path('searchReport', searchReport, name='searchReport'),
    path('admin/', admin.site.urls),
    path('signup', views.registration, name='signup'),
    path('login/', views.LoginPage, name='login'),
    # path('home/', views.HomePage, name='home'),
    # path('logout/', views.LogoutPage, name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
