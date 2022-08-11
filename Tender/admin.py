from django.contrib import admin
from Tender.models import Companydetails

# Register your models here.
class Tadmin(admin.ModelAdmin):
    list=['Company_Name','Company_Type','Address','GST','PAN','Company_Details','Company_Quote']

admin.site.register(Companydetails,Tadmin)