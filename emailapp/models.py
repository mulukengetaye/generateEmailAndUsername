
from django.db import models

class UserProfile1(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    # Additional fields if needed

    def __str__(self):
        return self.username
