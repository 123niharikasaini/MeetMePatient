from django.shortcuts import render,HttpResponse,redirect
from core.models import Patient,Doctor,Appointment
from django.contrib import messages
from django.contrib.auth.models import User
# for adding data in accountCreatedOn
from django.utils import timezone
from django.contrib.auth.hashers import check_password 

from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def domain(request):
    return render(request,"domain.html")

def contact(request):
    return render(request,"contact.html")

def services(request):
    return render(request,"services.html")

def signIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        # creating object of patient and doctor
        # to check for authenticity
        patient=Patient.objects.filter(patUserName=username).first()
        doctor=Doctor.objects.filter(docUserName=username).first()

        if patient and check_password(password, patient.password):
            user = authenticate(request, username=patient.patUserName, password=password)
            if user is not None:
                login(request, user)
                return redirect("domain")  
            else:
                messages.error(request, 'Invalid login credentials')

        elif doctor and check_password(password, doctor.password):
            user = authenticate(request, username=doctor.docUserName, password=password)
            if user is not None:
                login(request, user)
                return redirect("docProfile")  
            else:
                messages.error(request, 'Invalid login credentials')

        else:
                messages.error(request, 'Invalid login credentials')
    return render(request,'signin.html')
    

def option(request):
    return render(request,"option.html")



def patSignUp(request):
    if request.method=="POST":
        username=request.POST.get("username")
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        age=request.POST.get("age")
        g=request.POST.get("gender")

        if pass1==pass2:
            if Patient.objects.filter(patUserName=username).exists():
                messages.info(request,"Username taken")
                return redirect("patSignUp")
            else:   
            # obj of model
                
                user=Patient(patUserName=username,name=name,mobile=mobile,email=email,password=pass1,age=age,gender=g,AccountCreatedOn=timezone.now())
                user.save()
                messages.success(request,"Account created successfully... Please login again")
                return render(request,"index.html")
        else:
            messages.info(request,"password not matching")
            return redirect("patSignUp")


    return render(request,"signup.html")
    

def docSignUp(request):
    if request.method=="POST":
        username=request.POST.get("docUsername")
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        pass1=request.POST.get("pass1")
        pass2=request.POST.get("pass2")
        age=request.POST.get("age")
        g=request.POST.get("gender")
        degree=request.POST.get("degree")
        Specialization=request.POST.get("Specialization")
        Experience=request.POST.get("Experience")
        desc=request.POST.get("des")


        if pass1==pass2:
            if Doctor.objects.filter(docUserName=username).exists():
                messages.info(request,"Username taken")
                return redirect("docSignUp")
            else:   
            # obj of model
                
                user=Doctor(docUserName=username,name=name,mobile=mobile,email=email,password=pass1,age=age,gender=g,degree=degree,specialization=Specialization,experience=Experience,description=desc,AccountCreatedOn=timezone.now(),updatedOn=timezone.now())
                user.save()
                messages.success(request,"Account created successfully... Please login again")
                return render(request,"index.html")
        else:
            messages.info(request,"password not matching")
            return redirect("docSignUp")


    return render(request,"docSignUp.html")

def docProfile(request):
    pass

def fixAppointment(request):
    if request.method=="POST":
        pass
    return render(request,"appointment.html",)

def neurology(request):
    return render(request,"neurology.html")

def oncology(request):
    return render(request,"oncology.html")

def ophthalmologist(request):
    return render(request,"ophthalmologist.html")

def cardiology(request):
    return render(request,"cardiology.html")

def therapist(request):
    return render(request,"therapist.html")

def podiatrist(request):
    return render(request,"podiatrist.html")

def signOut(request):
    logout(request)
    return redirect('')
