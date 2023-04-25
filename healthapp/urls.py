from django.urls import path, include
from .views import AppointmentListView


urlpatterns = [
    path('', AppointmentListView.as_view(), name="appointment"),
    

]