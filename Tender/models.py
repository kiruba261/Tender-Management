import datetime
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.utils import timezone


# Create your models here.
class Companydetails(models.Model):
    Company_Name=models.CharField(max_length=25)
    Company_Type=models.CharField(max_length=20)
    Address=models.CharField(max_length=50)
    GST=models.CharField(max_length=25)
    PAN=models.CharField(max_length=10)
    Company_Details=models.CharField(max_length=70)
    Company_Quote=models.FileField()
    dateposted=models.DateTimeField(auto_now_add=True)