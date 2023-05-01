from django.contrib import admin
from django.urls import path, include
from api.views import(PatientList, PatientDetail, 
                      DoctorList, DoctorDetail, 
                      AppointmentList, AppointmentDetail,
                        BillingList, BillingDetail)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('patient/', PatientList.as_view(), name="patient-list"),
    path('patient/<int:pk>/', PatientDetail.as_view(), name="patient-detail"),
    path('doctor/', DoctorList.as_view(), name="doctor-list"),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name="doctor-detail"),
    path('appointment/', AppointmentList.as_view(), name="appointment-list"),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name="appointment-detail"),    
    path('billing/', BillingList.as_view(), name="billing-list"),
    path('billing/<int:pk>/', BillingDetail.as_view(), name="billing-detail"),    
]
