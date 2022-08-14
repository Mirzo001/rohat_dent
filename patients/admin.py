from django.contrib import admin

from patients.models import Patient, PatientBill, PatientVisit
from admin_searchable_dropdown.filters import AutocompleteFilter


class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['name']    
    
    
admin.site.register(Patient, PatientAdmin)
admin.site.register(PatientVisit)
admin.site.register(PatientBill)


