from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import hospital,doctor
# Create your views here. 
def index(request):
    hospital_table = hospital.objects.all()
    doctor_table = doctor.objects.all()
    return render(request,'events/base.html',{'hospital_table':hospital_table,'doctor_table':doctor_table})   
def hospital_home(request):
    hospital_table = hospital.objects.all()
    return render(request, 'events/hospital.html',{'hospital_table':hospital_table})
def doctor_home(request):
    doctor_table = doctor.objects.all()
    return render(request, 'events/doctor.html',{'doctor_table':doctor_table})
def info(request,id):
    hospital_info = hospital.objects.get(pk = id)
    return render(request, 'events/info.html',{'hospital_info': hospital_info})
def jin(request,id):
    doctor_jin = doctor.objects.filter(Doctor_id = id).first()
    return render(request, 'events/jin.html',{'doctor_jin' : doctor_jin})

    


        
        
