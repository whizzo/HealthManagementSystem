from django.contrib import admin
from .models import Patient, Doctor, Appointment, Billing


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Billing)


# Register your models here.
