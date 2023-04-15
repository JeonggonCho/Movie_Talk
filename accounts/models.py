from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField(blank=False, null=False)
    profile_image = models.ImageField(blank=True)