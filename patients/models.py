from pickle import TRUE
from django.db import models
from django.utils import timezone

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)


class BaseInfo(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200, default='', blank=True)
    
    class Meta:
        abstract = True

class Patient(BaseInfo):
    date_recorded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class PatientVisit(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(default=timezone.now)
    visit_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.patient.name
    
class PatientBill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment_date = models.DateTimeField(default=timezone.now)
    amount = models.FloatField()
    payment_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.patient.name
