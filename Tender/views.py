
from django.shortcuts import render,redirect
import Tender
from Tender.models import Companydetails
from Tender.forms import Company_form

# Create your views here.
def Retrive (request):
    Tcompany=Companydetails.objects.all()
    return render(request,'Tender/index.html',{'Tcompany':Tcompany}) 

def createview(request):
    form=Company_form()
    if request.method == 'POST':
        form=Company_form(request.POST)
        if form.is_valid():
          form.save()
          return redirect('/details')
    return render(request,'Tender/create.html',{'form':form}) 


def delete_v(request,id):
    Tcompany=Companydetails.objects.get(id=id)
    Tcompany.delete()
    return redirect('/details')

def update_v(request,id):
    Tcompany=Companydetails.objects.get(id=id)
    if request.method == 'POST':
        form=Company_form(request.POST,instance=Tcompany) 
        if form.is_valid():
            form.save()
            return redirect('/details')
    return render(request,'Tender/update.html',{'Tcompany':Tcompany})
    
    

    
    