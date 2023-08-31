from django.db import models

# # Create your models here.
# class Build(models.Model):
#     BuildID=models.IntegerField()
#     ClientID=models.IntegerField()
#     BuildName=models.CharField(max_length=100,blank=False)
#     BuildStatus=models.CharField(max_length=100,blank=False)
#     BuildDeadline=models.DateField(blank=True,null=True)

#     def __str__(self):
#         return self.BuildName
    

# class Ticket(models.Model):
#     TicketID=models.IntegerField()
#     Priority=models.CharField(max_length=50,blank=True,null=True)
#     Status=models.CharField(max_length=50,blank=True,null=True)
#     DueDate=models.DateTimeField(null=True)
#     AssignedTo=models.IntegerField(null=True)
#     Title=models.CharField(max_length=1000,blank=True,null=True)
#     Description=models.TextField(blank=True,null=True)
#     created_date=models.DateTimeField(auto_now_add=True, blank=True,null=True)
#     created_by=models.CharField(max_length=100,blank=True,null=True)
#     modified_date=models.DateTimeField(auto_now_add=True, blank=True,null=True)
#     modified_by=models.CharField(max_length=100,blank=True,null=True)
#     Category=models.CharField(max_length=300,blank=True,null=True)
#     MODULE=models.CharField(max_length=300,blank=True,null=True)
#     PrimaryDEV=models.IntegerField(blank=True,null=True)
#     PrimaryQC=models.IntegerField(blank=True,null=True)
#     PrimaryBA=models.IntegerField(blank=True,null=True)
#     TicketOwner=models.IntegerField(blank=True,null=True)

#     def __str__(self):
#         return self.Title
    

    





