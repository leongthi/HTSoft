from django.shortcuts import render,get_object_or_404,redirect
from .models import Build,Ticket
from shared.models import Customer, Status
from . import api
from . import functions as ft

from dateutil import parser

# Create your views here.
def task_dashboard(request):
    builds=Build.objects.all().order_by('id')

    lst_build=ft.InitialBuild(api.builds_getall())    
    if lst_build is not None:
        for build in lst_build:

            check_build=Build.objects.filter(BuildID=build["BuildID"])
            
            if check_build:                
                continue
            
            else:
                BuildID=build["BuildID"]
                ClientID=build["ClientID"]
                BuildName=build["BuildName"]
                BuildStatus=build["Status"]
                BuildDeadline=parser.isoparse(build["DueDate"])
                
                b=Build(
                    BuildID=BuildID,
                    ClientID=ClientID,
                    BuildName=BuildName,
                    BuildStatus=BuildStatus,
                    BuildDeadline=BuildDeadline
                )

                b.save()
    context={
        'builds':builds
    }
    return render(request,"taskmanagement/task_dashboard.html",context)

def task_dashboard_buildUpdate(request,id):

    build=get_object_or_404(Build,pk=id)
    if build is None:
        return
    
    

def buildTickets(request,BuildID):
    
    tickets=Ticket.objects.all().order_by('TicketID')
    lst_ticket=ft.InitialBuild(api.builds_getall())   
    if lst_ticket is not None:
        for ticket in lst_ticket:

            check_ticket=Ticket.objects.filter(TicketID=ticket["TicketID"])
            
            if check_ticket:                
                continue
            
            else:
                TicketID=ticket["TicketID"]
                Priority=ticket["Priority"]
                Status=ticket["Status"]
                DueDate=parser.isoparse(ticket["DueDate"])
                AssignedTo=ticket["AssignedTo"]
                Title=ticket["Title"]
                Description=ticket["Description"]
                created_date=parser.isoparse(ticket["CreatedOn"])
                modified_date=parser.isoparse(ticket["ModifiedOn"])
                created_by=ticket["CreatedBy"]
                modified_by=ticket["ModifiedBy"]
                Category=ticket["Category"]
                MODULE=ticket["MODULE"]
                PrimaryDEV=ticket["PrimaryDEV"]
                PrimaryQC=ticket["PrimaryQC"]
                PrimaryBA=ticket["PrimaryBA"]
                TicketOwner=ticket["TicketOwner"]
                
                tick=Ticket(
                    TicketID=TicketID,
                    Priority=Priority,
                    Status=Status,
                    DueDate=DueDate,
                    AssignedTo=AssignedTo,
                    Title=Title,
                    Description=Description,
                    created_date=created_date,
                    modified_date=modified_date,
                    created_by=created_by,
                    modified_by=modified_by,
                    Category=Category,
                    MODULE=MODULE,
                    PrimaryDEV=PrimaryDEV,
                    PrimaryQC=PrimaryQC,
                    PrimaryBA=PrimaryBA,
                    TicketOwner=TicketOwner,
                )

                tick.save()
    context={
        'tickets':tickets
    }
    return render(request,"taskmanagement/buildTickets.html",context)
    