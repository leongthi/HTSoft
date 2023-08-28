from django.db import models
from django.contrib.auth.models import User
from shared.models import Customer,Status

# Create your models here.
class Build(models.Model):
    BuildName=models.CharField(max_length=100,blank=False)
    BuildCustomerID=models.ForeignKey(Customer,related_name='build_Customer_2BuildCustomerID',on_delete=models.CASCADE)
    BuildStatusID=models.ForeignKey(Status,related_name='build_Status_2BuildStatusID',on_delete=models.CASCADE)
    BuildDeadline=models.DateField()
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.ForeignKey(User,related_name='user_Build_2created_by',on_delete=models.CASCADE)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.ForeignKey(User,related_name='user_Build_2modified_by',on_delete=models.CASCADE)

    def __str__(self):
        return self.BuildName