from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.

# custom user with specified field 
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id )+ ' : ' + self.email


