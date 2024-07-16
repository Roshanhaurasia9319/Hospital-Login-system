from django.db import models

# Create your models here.
class Doctor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    ProfilePicture = models.ImageField(upload_to='images/', default=None)
    Username = models.CharField(max_length=50)
    Email = models.EmailField(primary_key=True ,max_length=254)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=100, default=None)
    City = models.CharField(max_length=50, default=None)
    State = models.CharField(max_length=50, default=None)
    Pincode = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.Email

class Patient(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    ProfilePicture = models.ImageField(upload_to='images/', default=None)
    Username = models.CharField(max_length=50)
    Email = models.EmailField(primary_key=True ,max_length=254)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=100, default=None)
    City = models.CharField(max_length=50, default=None)
    State = models.CharField(max_length=50, default=None)
    Pincode = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.Email


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
       
       
STATUS = ((0,'Draft'),(1,'Published'))

       
class DoctorBlog(models.Model):
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    summary=models.TextField()
    content=models.TextField()
    status=models.IntegerField(choices=STATUS,default=0)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateField(auto_now_add=True)
    
    
    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return self.title
    
    
  
    
    
    