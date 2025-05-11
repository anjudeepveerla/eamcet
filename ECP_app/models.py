from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return self.user.email
