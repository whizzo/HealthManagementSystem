from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment, Billing
from django.contrib.auth import authenticate, login
from .forms import  PatientSignUpForm
from django.contrib.auth.decorators import permission_required

# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})   


def patient_signup(request):
    if request.method == "POST":
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            return redirect('home')
        else:
            form = PatientSignUpForm()
        return render(request, {'form': form})


def patient_list(request):
    patients = Patient.objects.all()
    context = {'paients': patients}
    return render(request, 'patient_list.html', context)


def patient_detail(request, pk):
    patient = Patient.objects.get(pk=pk)
    context = {'patient': patient}
    return render(request, 'patient_detail.html', context)

@permission_required('doctor.can_create_billing')
def create_billing(request, appointment_id):
    appointment = Appointment.objects.get(pk=appointment_id)


# Create your views here.
