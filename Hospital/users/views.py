from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Doctor, Patient, DoctorBlog, Category
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
                request.session['doctor_data']={
                    'FirstName':doctor.FirstName,
                    'LastName':doctor.LastName,
                    # 'ProfilePicture':doctor.ProfilePicture,
                    'Username':doctor.Username,
                    'Email':doctor.Email,
                    'Address':doctor.Address,
                    'City':doctor.City,
                    'State':doctor.State,
                    'Pincode':doctor.Pincode
                }
                blogs = DoctorBlog.objects.filter(doctor=Email)
                
                context = {
                    'user': doctor,
                    'blogs':blogs
                    
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
                context = {
                    'user': patient
                }
                messages.success(request, "Patient Login Successfully")
                return render(request, 'users/dashboard.html', context)
            else:
                messages.success(request, "Invalid Credentials")
                return redirect('patient')
        except Doctor.DoesNotExist:
            messages.success(request, "Doctor Email Do Not Exist")
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

        # Retrieve doctor and category objects
        try:
            doctor = Doctor.objects.get(Email=doctor_email)
        except Doctor.DoesNotExist:
            messages.error(request, 'Doctor not found')
            return redirect('add_blog')  # Adjust the redirect as per your URL names

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, 'Category not found')
            return redirect('add_blog')  # Adjust the redirect as per your URL names

        # Create new blog
        new_blog = DoctorBlog(
            doctor=doctor, 
            title=title, 
            image=image, 
            category=category, 
            summary=summary,
            content=content, 
            status=status
        )
        new_blog.save()

        # Get doctor data from session
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

            # Filter blogs for the doctor with the email stored in the session
            blogs = DoctorBlog.objects.filter(doctor__Email=doctor_data['Email'])

            context = {
                'user': doctor_detail,
                'blogs': blogs
            }

            messages.success(request, 'Blog post created successfully!')
            return render(request, 'users/dashboard.html', context)

    # GET request
    doctors = Doctor.objects.filter(Email=doctor_data['Email'])
    categories = Category.objects.all()
    context = {
        'doctors': doctors,
        'categories': categories
    }

    return render(request, 'users/AddBlog.html', context)







def blogs(request):
    blogs = DoctorBlog.objects.filter(status=1)
    context={
        'blogs':blogs
    }
    return render(request, 'users/blogs.html', context)