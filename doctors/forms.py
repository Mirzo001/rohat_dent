from django import forms

from .models import Appointment

class AppointmentEditForm(forms.ModelForm):
  
    class Meta:
        model = Appointment
        fields = ('doctor','patient','date', 'time','status')
        

# class AppointmentCreateForm(forms.ModelForm):
  
#     class Meta:
#         model = Appointment
#         fields = ('doctor','patient','date', 'time','status')