from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from healthapp.models import Patient, Doctor, Appointment, Billing
from django import forms




class PatientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_number', 'date_of_birth', 'address']
        extra_kwargs = {'password': {'write_only': True}, 'confirm_password': {'write_only': True}}
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),

        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords don't match")
        patient = Patient.objects.create(**validated_data)
        patient.set_password(password)
        patient.save()
        return patient
    

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            patient = authenticate(email=email, password=password)
            if patient:
                if not patient.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
                attrs['patient']= patient
            else:
                msg= _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password". ')
            raise serializers.ValidationError(msg)
        
        return attrs
    

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

@api_view(['POST'])
def signup(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing
        fields = '__all__'