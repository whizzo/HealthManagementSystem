from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from api.views import(PatientList, PatientDetail, 
                      DoctorList, DoctorDetail, 
                      AppointmentList, AppointmentDetail,
                        BillingList, BillingDetail, PatientLoginView)
from api.serializers import PatientViewSet, signup
from healthapp.views import patient_signup

# import api.urls



router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/login/', PatientLoginView.as_view(), name='patient_login'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('patient/', PatientList.as_view(), name="patient-list"),
    path('patient/<int:pk>/', PatientDetail.as_view(), name="patient-detail"),
    path('doctor/', DoctorList.as_view(), name="doctor-list"),
    path('doctor/<int:pk>/', DoctorDetail.as_view(), name="doctor-detail"),
    path('appointment/', AppointmentList.as_view(), name="appointment-list"),
    path('appointment/<int:pk>/', AppointmentDetail.as_view(), name="appointment-detail"),    
    path('billing/', BillingList.as_view(), name="billing-list"),
    path('billing/<int:pk>/', BillingDetail.as_view(), name="billing-detail"),
    path('patient/signup', PatientList.as_view(),),    
]
