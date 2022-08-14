from django.db import models
from django.utils import timezone

from patients.models import Patient
from accounts.models import CustomUser

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

STAFF_CHOICES = (
    ("Dentist", "Dentist"),
    ("Nurse", "Nurse"),
    ("Dentist", "Technican"),
)

class BaseInfo(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    
    class Meta:
        abstract = True
        
class Doctor(BaseInfo):
    position = models.CharField(max_length=100, choices=STAFF_CHOICES)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    

STATUS_CHOICES = (
    ("Completed", "Completed"),
    ("Pending", "Pending"),
    ("Cancelled", "Cancelled"),
)
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)

    class Meta:
        ordering = ('time',)
        
    # def __str__(self):
    #     return self.date.strftime('%d %b %Y %H:%M:%S')
    def __str__(self):
        return self.time.strftime('%H:%M')

    
class Time(models.Model):
    time = models.TimeField()
    
    def __str__(self):
        return self.time.strftime('%H:%M')
    class Meta:
        ordering = ('time',)