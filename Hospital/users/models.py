from django.db import models

# Create your models here.
class Doctor(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    ProfilePicture = models.ImageField(upload_to='profile_images/')
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
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
    ProfilePicture = models.ImageField(upload_to='profile_images/')
    Username = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=20)
    Address = models.CharField(max_length=100, default=None)
    City = models.CharField(max_length=50, default=None)
    State = models.CharField(max_length=50, default=None)
    Pincode = models.CharField(max_length=10, default=None)

    def __str__(self):
        return self.Email
