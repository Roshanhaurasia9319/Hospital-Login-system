from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doctor', views.doctor, name="doctor"),
    path('patient', views.patient, name='patient'),
    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('patient/login/', views.patient_login, name='patient_login'),
]