from django.db import models

# Create your models here.
class Build(models.Model):
    BuildID=models.IntegerField()
    ClientID=models.IntegerField()
    BuildName=models.CharField(max_length=100,blank=False)
    BuildStatus=models.CharField(max_length=100,blank=False)
    BuildDeadline=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.BuildName
    

class Ticket(models.Model):
    TicketID=models.IntegerField()
    Priority=models.CharField(max_length=50,blank=True)
    Status=models.CharField(max_length=50,blank=True)
    DueDate=models.DateTimeField()
    AssignedTo=models.IntegerField()
    Title=models.CharField(max_length=1000,blank=True)
    Description=models.CharField(max_length=3000,blank=True)
    created_date=models.DateTimeField(auto_now_add=True, blank=True)
    created_by=models.CharField(max_length=100,blank=True)
    modified_date=models.DateTimeField(auto_now_add=True, blank=True)
    modified_by=models.CharField(max_length=100,blank=True)
    Category=models.CharField(max_length=300,blank=True)
    MODULE=models.CharField(max_length=300,blank=True)
    PrimaryDEV=models.IntegerField()
    PrimaryQC=models.IntegerField()
    PrimaryBA=models.IntegerField()
    TicketOwner=models.IntegerField()

    def __str__(self):
        return self.Title


