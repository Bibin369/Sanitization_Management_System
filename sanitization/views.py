import random
from datetime import date

from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout, login
from datetime import date


# Create your views here.

def index(request):
    services = Services.objects.all()
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')

#
def registration(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        ud = sign_up(name=fname,addr=addr,email=email,contact=contact,password=password)
        ud.save()
        context = {'msg': 'User Registered'}
        return render(request, 'index.html', context)

    else:
        return render(request, 'signup.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)

        user=sign_up.objects.filter(email=username, password=pass1)
        print(user)

        if len(user) == 1:
            print("logined")
            request.session['user_name'] = user[0].email
            services = Services.objects.all()

            return render(request, 'index2.html', locals())
        else:
            print("not logined")
            return render (request,'login.html')
    return render (request,'login.html')

def index2(request):
    services = Services.objects.all()

    return render(request, 'index2.html',locals())
def servicereq(request, pid):
    services = Services.objects.get(id=pid)
    if request.method == "POST":
        trn = str(random.randint(10000000, 99999999))
        fname = request.POST['FirstName']
        emailid = request.POST['EmailId']
        dateofSanitization = request.POST['DateofSanitization']
        timeofSanitization = request.POST['TimeofSanitization']
        mob = request.POST['MobileNumber']
        address = request.POST['Address']
        state = request.POST['State']
        city = request.POST['City']
        message = request.POST['Message']

        user = User.objects.create_user(username=emailid, first_name=fname)
        Requests.objects.create(user=user, service=services, RequestID=trn, DateofSanitization=dateofSanitization,
                                TimeofSanitization=timeofSanitization, MobileNumber=mob, Address=address, State=state,
                                City=city, Message=message)
        try:
            error = "no"
        except:
            error = "yes"
    return render(request, 'servicereq.html', locals())


def contact(request):
    return render(request, 'contact.html')

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', locals())


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    totalserv = Services.objects.all().count()
    totalnewreq = Requests.objects.filter(Status__isnull=True).count()
    totalontheway = Requests.objects.filter(Status='Team On The Way').count()
    totalinprocess = Requests.objects.filter(Status='Request is inprocess').count()
    totalreq = Requests.objects.all().count()
    totalrejectreq = Requests.objects.filter(Status='Request has been rejected').count()
    totalcomreq = Requests.objects.filter(Status='Request has been Completed').count()
    return render(request, 'dashboard.html', locals())


def add_Service(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.all()
    try:
        if request.method == "POST":
            sname = request.POST['ServiceName']
            price = request.POST['Price']
            serviceDetail = request.POST['ServiceDetail']
            image = request.FILES['Image']

            try:
                Services.objects.create(ServiceName=sname, Price=price, ServiceDetail=serviceDetail, Image=image)
                error = "no"
            except:
                error = "yes"
    except:
        pass
    return render(request, 'add_Service.html', locals())


def editService(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    service = Services.objects.get(id=pid)
    if request.method == "POST":
        sname = request.POST['ServiceName']
        price = request.POST['Price']
        serviceDetail = request.POST['ServiceDetail']

        service.ServiceName = sname
        service.Price = price
        service.ServiceDetail = serviceDetail

        try:
            service.save()
            error = "no"
        except:
            error = "yes"

        try:
            image = request.FILES['Image']
            service.Image = image
            service.save()
        except:
            pass
    return render(request, 'editService.html', locals())


def deleteService(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    service = Services.objects.get(id=pid)
    service.delete()
    return redirect('add_Service')

def newRequest(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.filter(Status__isnull=True)
    return render(request, 'newRequest.html', locals())

def request_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.get(id=pid)
    track1 = Tracking.objects.filter(request=requests)
    requestid = requests.id
    reportcount = Tracking.objects.filter(request=requests).count()

    if request.method == "POST":
        Status = request.POST['Status']
        Remark = request.POST['Remark']

        try:
            tracking = Tracking.objects.create(request=requests,Remark=Remark, Status=Status)
            requests.Status = Status
            requests.Remark = Remark
            requests.UpdationDate = date.today()
            requests.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'request_details.html', locals())

def onthewayReq(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.filter(Status='Team On The Way')
    return render(request, 'onthewayReq.html', locals())

def inprocessReq(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.filter(Status='Request is inprocess')
    return render(request, 'inprocessReq.html', locals())

def rejectReq(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.filter(Status='Request has been rejected')
    return render(request, 'rejectReq.html', locals())

def completeReq(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.filter(Status='Request has been Completed')
    return render(request, 'completeReq.html', locals())

def allReq(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.all()
    return render(request, 'allReq.html', locals())

def deleteReq(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    requests = Requests.objects.get(id=pid)
    requests.delete()
    return redirect('allReq')


def bwdateReport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['FromDate']
        td = request.POST['ToDate']

        requests = Requests.objects.filter(Q(RequestDate__gte=fd) & Q(RequestDate__lte=td))
        return render(request, 'bwdatesReportDtls.html', locals())
    return render(request, 'bwdateReport.html')

def searchReport(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        test = Requests.objects.filter(Q(RequestID=sd) | Q(MobileNumber=sd))
    except:
        test = ""
    return render(request,'searchReport.html', locals())


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())


def Logout(request):
    logout(request)
    return redirect('index')

def track(request):
    sd = None
    if request.method == 'POST':
        sd = request.POST['searchdata']
    try:
        test = Requests.objects.filter(Q(RequestID=sd) | Q(MobileNumber=sd))
    except:
        test = ""
    return render(request,'track.html', locals())


