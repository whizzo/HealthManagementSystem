from django.shortcuts import render
from django.views.generic import ListView
from .models import Appointment, Patient, Doctor, Billing


class AppointmentListView(ListView):
    model = Appointment
    template_name = "appointment.html"

class PatientListView(ListView):
    model = Patient
    template_name = 'patient.html'

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor.html'

class BillingListView(ListView):
    model = Billing
    template_name = 'billing.html'


# Create your views here.
