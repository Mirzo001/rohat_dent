
from django.urls import path

from .views import PatientListView, CreatePatientView

appname = "patients"

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patients'),
    path('patients/new/', CreatePatientView.as_view(), name='patients_new'),
]
