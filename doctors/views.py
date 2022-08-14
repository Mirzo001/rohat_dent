
import django
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from doctors.forms import AppointmentEditForm
from doctors.models import STATUS_CHOICES, Appointment, Doctor,Time
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse
# class HomePageView(TemplateView):
#     template_name = 'base.html'

from datetime import datetime, timedelta

# def datetime_range(start, end, delta):
#     current = start
#     while current < end:
#         yield current
#         current += delta

# dts = [dt.strftime('%H:%M') for dt in 
#        datetime_range(datetime(2022, 9, 1, 6), datetime(2022, 9, 1, 23), 
#        timedelta(hours=1))]

class AppointmentListView(LoginRequiredMixin,ListView ):
    model = Appointment
    template_name = 'dashboard.html'

    def get_context_data(self,**kwargs):
        
        appointment = Appointment.objects.all()
        time = Time.objects.all()
        query = self.request.GET.get('q','')
        if query:
            appointment = self.model.objects.filter(patient__name__icontains=query)
    
        context = super(AppointmentListView,self).get_context_data(**kwargs)
        context={
         
            'appointment':appointment,
            'time':time,
            'query':query,
        }
        return context
    

class AppointmentDetail(LoginRequiredMixin,DetailView ):
    model = Appointment
    template_name = 'appointment/appointment_detail.html'
    
class CreateAppointmentView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Appointment
    template_name = 'appointment/appointment_new.html'
    fields = ['patient', 'date','time','status','doctor']
    
    def test_func(self):
        return self.request.user.is_staff
    
    # def form_valid(self, form):
    #     form.instance.doctor.user = self.request.user
    #     return super().form_valid(form)
    
   
    success_url = reverse_lazy('dashboard')


class HomeView(TemplateView):
    template_name = 'home.html'
    
# shu yerda statusga qarab increment bo'ladi
# class EditAppointmentView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
#     model = Appointment
#     fields = '__all__'
#     template_name = 'appointment/appointment_edit.html'

#     def get(self, request, appointment_id):
        
    
#     def test_func(self):
#         obj = self.get_object() 
#         return obj.doctor.user == self.request.user
#     success_url = reverse_lazy('dashboard')


        
    
class EditAppointmentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        print(appointment)
        appointment_form = AppointmentEditForm(instance=appointment)
        if appointment.status == "Completed":
        #     appointment_form.fields['status'].disabled=True
            appointment_form.fields['status'].disabled = True
            # status = appointment_form.status(disabled = True)
        return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form})

    def post(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment_form = AppointmentEditForm(instance=appointment, data=request.POST)
        # appointment_form.save()
        
        if appointment_form.is_valid():
            appointment_form.save()
            
            return redirect(reverse_lazy('dashboard'))
        print(request.POST)
        return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form})

    
    
class DoctorProfileView(TemplateView):
    model = Doctor
    template_name = 'doctor_profile.html'
    
    
def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = Appointment.objects.filter(patient__name__icontains=query_original)
    print(queryset)
    mylist = []
    mylist += [x.patient.name for x in queryset] 
    return JsonResponse(mylist, safe=False)  
