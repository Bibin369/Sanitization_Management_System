from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class sign_up(models.Model):

    name = models.CharField(max_length=100, )
    addr = models.CharField(max_length=500)
    contact = models.IntegerField()
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=100)


class Services(models.Model):
    ServiceName = models.CharField(max_length=250, null=True)
    Price = models.CharField(max_length=200, null=True)
    Image = models.FileField(max_length=150, null=True)
    ServiceDetail = models.CharField(max_length=350, null=True)
    CreationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ServiceName


class Requests(models.Model):
    RequestID = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    DateofSanitization = models.DateField(null=True)
    TimeofSanitization = models.TimeField(null=True)
    Address = models.CharField(max_length=250, null=True)
    MobileNumber = models.CharField(max_length=15, null=True)
    State = models.CharField(max_length=150, null=True)
    City = models.CharField(max_length=150, null=True)
    Message = models.CharField(max_length=350, null=True)
    RequestDate = models.DateTimeField(auto_now_add=True)
    Remark = models.CharField(max_length=250, null=True)
    Status = models.CharField(max_length=100, null=True)
    UpdationDate = models.DateField(null=True)

    def __str__(self):
        return self.user.first_name

class Tracking(models.Model):
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
    Remark = models.CharField(max_length=350, null=True)
    Status = models.CharField(max_length=100, null=True)
    UpdationDate = models.DateTimeField(auto_now_add=True)
