from django.db import models


class UserTicket(models.Model):
    ID_main=models.IntegerField(null=True,blank=True)
    Responsibility=models.CharField(max_length=255,null=True,blank=True)
    FirstName=models.CharField(max_length=255,null=True,blank=True)
    Email=models.CharField(max_length=255,null=True,blank=True)
    UserName=models.CharField(max_length=255,null=True,blank=True)
    PASSWORD=models.CharField(max_length=255,null=True,blank=True)
    IsActive=models.BooleanField(null=True,blank=True)

    def __str__(self):
        return self.Responsibility+'-'+self.FirstName

