from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ips = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    num_attacks = models.IntegerField(default=0)

    # Add any other fields you need for user-specific data

    def __str__(self):
        return self.user.username