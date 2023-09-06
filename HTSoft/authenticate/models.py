from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    avatar=models.ImageField(null=True,blank=True)
    MapUserTicket=models.IntegerField(null=True,blank=True)