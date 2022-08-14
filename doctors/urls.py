from django.urls import path
from .views import AppointmentDetail, AppointmentListView, DoctorProfileView, HomeView, CreateAppointmentView, EditAppointmentView, autosuggest

urlpatterns = [
    
    path('dashboard/', AppointmentListView.as_view(), name='dashboard'),
    path("autosuggest/", autosuggest, name="autosuggest"),
    path('', HomeView.as_view(), name='home'),
    path('new/', CreateAppointmentView.as_view(), name='appointment_new'),
    path('<int:pk>/edit/', EditAppointmentView.as_view(), name='appointment_edit'),
    path('<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),
    path('doctor-profile/', DoctorProfileView.as_view(), name='doctor_profile',)
    # path("register/", RegisterView.as_view(), name="register"),
]