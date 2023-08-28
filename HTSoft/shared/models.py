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


# class Build(models.Model):
#     BuildName=models.CharField(max_length=100,blank=False)
#     BuildCustomerID=models.ForeignKey(Customer,related_name='build_Customer_2BuildStatus',on_delete=models.CASCADE)
#     BuildStatus=models.ForeignKey(Status,related_name='build_Status_2BuildStatus',on_delete=models.CASCADE)
#     Deadline=models.DateField()
#     created_date=models.DateTimeField(auto_now_add=True, blank=True)
#     created_by=models.ForeignKey(User,related_name='user_Build_2created_by',on_delete=models.CASCADE)
#     modified_date=models.DateTimeField(auto_now_add=True, blank=True)
#     modified_by=models.ForeignKey(User,related_name='user_Build_2modified_by',on_delete=models.CASCADE)

#     def __str__(self):
#         return self.BuildName