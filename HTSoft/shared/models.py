from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    CustomerNo=models.CharField(max_length=20,blank=False)
    CustomerName=models.CharField(max_length=300,blank=False)
    HospitalCouncil=models.CharField(max_length=200,blank=True)
    CustomerAddress=models.CharField(max_length=500,blank=False)
    Hotline=models.CharField(max_length=50,blank=True)
    Email=models.CharField(max_length=50,blank=True)
    Website=models.CharField(max_length=50,blank=True)
    Logo=models.ImageField(blank=True)
    IsActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Customer_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Customer_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.CustomerName
class Status(models.Model):
    StatusName=models.CharField(max_length=100,blank=False)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Status_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Status_2modified_by',on_delete=models.CASCADE)


    def __str__(self):
        return self.StatusName


class Client(models.Model):
    ClientName=models.CharField(max_length=100,blank=False)
    IsActive=models.BooleanField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Client_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Client_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.ClientName
    
class UsersTicket(models.Model):
    UserID =models.IntegerField()
    Responsibility=models.CharField(max_length=100,blank=True,null=True)
    FirstName=models.CharField(max_length=100,blank=True,null=True)
    LastName=models.CharField(max_length=100,blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)
    PasswordEmail=models.CharField(max_length=256,blank=True,null=True)
    Tel=models.CharField(max_length=50,blank=True,null=True)
    ClientID=models.IntegerField(blank=True,null=True)
    UserName=models.CharField(max_length=100,blank=True,null=True)
    PASSWORD=models.CharField(max_length=100,blank=True,null=True)
    Skype=models.CharField(max_length=100,blank=True,null=True)
    IsActive=models.BooleanField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    created_by=models.CharField(max_length=100,blank=True,null=True)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    modified_by=models.CharField(max_length=100,blank=True,null=True)
    NewID=models.CharField(max_length=50,unique=True,blank=True,null=True)

    def __str__(self):
        return f"{self.Responsibility} - {self.FirstName}"