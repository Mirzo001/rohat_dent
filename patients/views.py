from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from doctors.models import Appointment, Patient
from django.urls import reverse_lazy


class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patients/patients.html'
    def get_context_data(self,**kwargs):
        patients = Patient.objects.all()
        appointments = Appointment.objects.all()
        # time = Time.objects.all()
        
        context = super(PatientListView,self).get_context_data(**kwargs)
        context={
            'patients': patients,
            'appointments':appointments,
        } 
        return context
    
class CreatePatientView(LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patients/patients_new.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user.is_superuser
    success_url = reverse_lazy('patients')
    

# class EditPatientView(UserPassesTestMixin, LoginRequiredMixin,UpdateView):
#     model = Patient
#     fields = '__all__'
#     template_name = 'appointment/appointment_edit.html'

#     def test_func(self):
#         obj = self.get_object() 
#         return obj.doctor.user == self.request.user
#     success_url = reverse_lazy('patients')