
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        location = models.CharField(max_length=140, blank=True)
        bio = models.TextField(blank=True)
        profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
        
        def __str__(self):
            return f"Profile of user: {self.user.username}"