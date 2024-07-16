from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name='patient'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),  
    path('patient/login/', views.patient_login, name='patient_login'),
    path('doctor/login/AddBlog', views.add_doctor_blog, name='add_doctor_blog'),
    path('blogs', views.blogs, name='blogs'),
]

