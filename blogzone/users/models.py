# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings 

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.username
