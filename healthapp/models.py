from django.db import models
from django.urls import reverse

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=200)

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    specialty = models.CharField(max_length=100)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models = models.ForeignKey(Doctor, on_delete=models.CASCADE)
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
