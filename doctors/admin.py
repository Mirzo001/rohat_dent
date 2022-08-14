from django.contrib import admin
from doctors.models import Appointment, Doctor, Time

# admin.site.register(Appointment)
admin.site.register(Time)

class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Doctor, DoctorAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['time']
    list_display = ['doctor', 'time', 'patient']
    list_filter = ['doctor']
    

    
admin.site.register(Appointment,AppointmentAdmin)