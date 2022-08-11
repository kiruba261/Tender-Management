from dataclasses import field
from django import forms
from Tender.models import Companydetails
# Create your models here.
 
class Company_form(forms.ModelForm):
    class Meta:
        model=Companydetails
      #  feilds=['Company_Name','Company_Type','Address','GST','PAN','Company_Details','Company_Quote']
        fields='__all__'
        exclude=['Company_Quote','dateposted']
       # fields=['Company_Name','Company_Type','Address','GST','PAN','Company_Details']    

    