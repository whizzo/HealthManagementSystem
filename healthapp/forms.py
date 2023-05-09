from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient



class PatientSignUpForm(UserCreationForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', "address"]
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
#     password1 = forms.CharField(widget=forms.PasswordInput)


