from django.db import models
from django.urls import reverse
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.hashers import make_password

# class User(AbstractUser):
#     is_patient = models.BooleanField(default=False)
#     is_doctor = models.BooleanField(default= False)


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50, blank=True, null=True, default="some_value")
    confirm_password = models.CharField(max_length=50, blank=True, null=True, default="some_value")
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)
    def set_password(self, password):
        self.password = make_password(password)   
    # class Meta:
    #     permissions = [
    #         ("can_create_appointment", _("Can create appointment")),
    #     ]
class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('doctor_detail', args=[str(self.id)])
    
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)
    symptoms = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.patient} - {self.doctor} - {self.appointment_date} - {self.appointment_time}"
    
    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])



class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
# Create your models here.
