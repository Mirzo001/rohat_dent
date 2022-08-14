from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # age = models.PositiveIntegerField(null=True, blank=True)
    profile_picture = models.ImageField(blank=True,default="default_profile_pic.jpg")
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
