from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import UserTicket

# Create your models here.
class CustomUser(AbstractUser):
    avatar=models.ImageField(upload_to='static/images/',null=True,blank=True)
    map_user_ticket = models.CharField(max_length=50,null=True,blank=True)