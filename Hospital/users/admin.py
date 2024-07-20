from django.contrib import admin
from .models import Doctor, Patient, DoctorBlog, Category, Appointment

# Register your models here.
# admin.site.register(Doctor)
admin.site.register(Patient)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'ProfilePicture', 'Username', 'Email', 
                    'Password', 'Address', 'City', 'State', 'Pincode')


class DoctorBlogAdmin(admin.ModelAdmin):
    list_display=('title','doctor', 'status', 'created_on')
    list_filter=('status',)
    search_fields=['title', 'content']
    

admin.site.register(DoctorBlog, DoctorBlogAdmin)
admin.site.register(Category)

admin.site.register(Appointment)