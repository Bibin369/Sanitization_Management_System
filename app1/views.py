from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from sanitization  import models
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

#
# def sign_up(request):
#     if request.method == 'POST':
#         n = request.POST.get('fname')
#         addr = request.POST.get('addr')
#         email = request.POST.get('email')
#         contact = request.POST.get('contact')
#         password = request.POST.get('password')
#
#         ud = sign_up(name=n,addr=addr,email=email,contact=contact,password=password)
#         ud.save()
#         context = {'msg': 'User Registered'}
#         return render(request, 'login.html', context)
#
#     else:
#         return render(request, 'signup.html')

#
# def LoginPage(request):
#
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         print(username,pass1)
#         user=User.authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             return HttpResponse ("Username or Password is incorrect!!!")
#     return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')