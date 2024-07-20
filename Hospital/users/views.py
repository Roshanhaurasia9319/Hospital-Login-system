from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Doctor, Patient, DoctorBlog, Category, Appointment
from google.oauth2 import service_account


# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def doctor(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        ProfilePicture = request.FILES.get('ProfilePicture')
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
            NewDoctor = Doctor(
                FirstName=FirstName, LastName=LastName, ProfilePicture=ProfilePicture,
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
        ProfilePicture = request.FILES.get('ProfilePicture')
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
                    NewPatient = Patient(
                        FirstName=FirstName, LastName=LastName, ProfilePicture=ProfilePicture,
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
                request.session['doctor_data'] = {
                    'FirstName': doctor.FirstName,
                    'LastName': doctor.LastName,
                    'Username': doctor.Username,
                    'Email': doctor.Email,
                    'Address': doctor.Address,
                    'City': doctor.City,
                    'State': doctor.State,
                    'Pincode': doctor.Pincode
                }
                blogs = DoctorBlog.objects.filter(doctor=Email)

                context = {
                    'user': doctor,
                    'blogs': blogs
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
                request.session['patient_data'] = {
                    'FirstName': patient.FirstName,
                    'LastName': patient.LastName,
                    'Username': patient.Username,
                    'Email': patient.Email,
                    'Address': patient.Address,
                    'City': patient.City,
                    'State': patient.State,
                    'Pincode': patient.Pincode
                }
                doctors = Doctor.objects.all()
                context = {
                    'user': patient,
                    'doctors': doctors
                }
                messages.success(request, "Patient Login Successfully")
                return render(request, 'users/patientDashboard.html', context)
            else:
                messages.success(request, "Invalid Credentials")
                return redirect('patient')
        except Patient.DoesNotExist:
            messages.success(request, "Patient Email Do Not Exist")
            return redirect('patient')

    return render(request, 'users/patient.html')

def dashboard(request):
    return render(request, 'users/dashboard.html')

def add_doctor_blog(request):
    doctor_data = request.session.get('doctor_data')
    if request.method == 'POST':
        doctor_email = request.POST.get('doctor')
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        status = request.POST.get('status')

        try:
            doctor = Doctor.objects.get(Email=doctor_email)
        except Doctor.DoesNotExist:
            messages.error(request, 'Doctor not found')
            return redirect('add_blog')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, 'Category not found')
            return redirect('add_blog')

        new_blog = DoctorBlog(
            doctor=doctor, title=title, image=image, category=category, summary=summary,
            content=content, status=status)
        new_blog.save()

        doctor_data = request.session.get('doctor_data')
        if doctor_data:
            doctor_detail = {
                'FirstName': doctor_data['FirstName'],
                'LastName': doctor_data['LastName'],
                'Username': doctor_data['Username'],
                'Email': doctor_data['Email'],
                'Address': doctor_data['Address'],
                'City': doctor_data['City'],
                'State': doctor_data['State'],
                'Pincode': doctor_data['Pincode']
            }

            blogs = DoctorBlog.objects.filter(doctor__Email=doctor_data['Email'])

            context = {
                'user': doctor_detail,
                'blogs': blogs
            }

            messages.success(request, 'Blog post created successfully!')
            return render(request, 'users/dashboard.html', context)

    doctors = Doctor.objects.filter(Email=doctor_data['Email'])
    categories = Category.objects.all()
    context = {
        'doctors': doctors,
        'categories': categories
    }

    return render(request, 'users/AddBlog.html', context)

def blogs(request):
    blogs = DoctorBlog.objects.filter(status=1)
    context = {
        'blogs': blogs
    }
    return render(request, 'users/blogs.html', context)




def book_appointment(request, email):
    doctor = Doctor.objects.get(Email=email)
    patient_data = request.session.get('patient_data')

    if request.method == 'POST':
        Speciality = request.POST.get('Speciality')
        Date = request.POST.get('Date')
        Time = request.POST.get('Time')

        newAppointment = Appointment(
            Speciality=Speciality, Date=Date, Time=Time)
        newAppointment.save()

        context = {
            'doctor': doctor,
            'newAppointment': newAppointment,
            'patient_data': patient_data
        }
        return render(request, 'users/appointmentDetail.html', context)

    context = {
        'doctor': doctor
    }

    return render(request, 'users/appointment.html', context)

def appointmentDetail(request):
    return render(request, 'users/appointmentDetail.html')
