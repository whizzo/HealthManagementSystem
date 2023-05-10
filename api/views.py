from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from healthapp.models import Patient, Doctor, Appointment, Billing
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, BillingSerializer
from django.http import JsonResponse



@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token/',
        '/api/token/refresh/',
    ]
    return Response(routes)

# @api_view(['POST'])
# def register_view(request):
#     serializer = PatientSerializer(data=request.data)
#     if serializer.is_valid():
#         if serializer.data.get('password') != serializer.
#         patient = serializer.save()
        

class PatientList(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentDetail(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class BillingList(generics.ListCreateAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class BillingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer

class PatientLoginView(ObtainAuthToken):
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        return Response({'detail': 'You must provide an email and password to log in.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        patient = serializer.validated_data['patient']
        token, created = Token.objects.get_or_create(user=patient)
        return Response({'token': token.key})



