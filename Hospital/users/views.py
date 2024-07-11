from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import Doctor, Patient
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def doctor(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        ProfilePicture = request.POST.get('ProfilePicture')
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('ConfirmPassword')
        Address = request.POST.get('Address')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Pincode = request.POST.get('Pincode')
        
        if Email:
            exist = Doctor.objects.filter(Email=Email).exists()
            if exist:
                messages.success(request, "Email Already Exists")
                return redirect(doctor)
                
        if Password != ConfirmPassword:
            return JsonResponse({'Password': 'Not equal'})
        else:
            NewDoctor = Doctor(FirstName=FirstName, LastName=LastName, ProfilePicture=ProfilePicture,
                               Username=Username, Email=Email, Password=Password, Address=Address,
                               City=City, State=State, Pincode=Pincode)
            messages.success(request, "Successfully Register By Doctor")
            NewDoctor.save()
            return redirect('index')

    return render(request, 'users/doctor.html')




def patient(request):
    
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        ProfilePicture = request.POST.get('ProfilePicture')
        Username = request.POST.get('Username')
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        ConfirmPassword = request.POST.get('ConfirmPassword')
        Address = request.POST.get('Address')
        City = request.POST.get('City')
        State = request.POST.get('State')
        Pincode = request.POST.get('Pincode')
        
        
        if Email:
            exist = Patient.objects.filter(Email=Email).exists()
            if exist:
                messages.success(request, "Email Already Exists")
                return redirect(patient)
            else:
                 if Password != ConfirmPassword:
                    return JsonResponse({'Password': 'Not equal'})
                 else:
                    NewPatient = Patient(FirstName=FirstName, LastName=LastName, ProfilePicture=ProfilePicture,
                               Username=Username, Email=Email, Password=Password, Address=Address,
                               City=City, State=State, Pincode=Pincode)
                    messages.success(request, "Successfully Register By Patient")
                    NewPatient.save()
                    return redirect('index')

       

    return render(request, 'users/patient.html')

def doctor_login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        try:
            doctor = Doctor.objects.get(Email=Email)
            if doctor.Password == Password:
                user = Doctor.objects.all()
                context={
                    'user':user,
                }
                messages.success(request, "Doctor Login Successfully")
                return render(request, 'users/dashboard.html', context)
            else:
                messages.success(request, "Invalid Credentials")
                return redirect('doctor')
        except Doctor.DoesNotExist:
            messages.success(request, "Doctor Email Do Not Exist")
            return redirect('doctor')

    return render(request, 'users/doctor.html')


def patient_login(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        try:
            patient = Patient.objects.get(Email=Email)
            if patient.Password == Password:
                user = Patient.objects.all()
                context={
                    'user':user,
                }
                messages.success(request, "Patient Login Successfully")
                return render(request, 'users/dashboard.html', context)
            else:
                messages.success(request, "Invalid Credentials")
                return redirect('patient')
        except Patient.DoesNotExist:
            messages.success(request, "Doctor Email Do Not Exist")
            return redirect('patient')

    return render(request, 'users/patient.html')
    
def dashboard(request):
    return render(request, 'users/dashboard.html')