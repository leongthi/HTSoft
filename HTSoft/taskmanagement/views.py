from django.shortcuts import render,get_object_or_404,redirect

from . import api
from . import functions as ft
from dateutil import parser
from django.db import connection

# Create your views here.
def task_dashboard(request):

    #Get build list
    builds=ft.Initial(api.builds_getall())


    context={
        'builds':builds
    }
    return render(request,"taskmanagement/task_dashboard.html",context)


    

def buildTickets(request,BuildID):
    
    tickets=ft.Initial(api.buildTicket_get(BuildID))
    
    for ticket in tickets:
        if ticket is None:
            tickets.remove(ticket)
    
    context={
        'tickets':tickets
        
    }
    return render(request,"taskmanagement/buildTickets.html",context)
    

def ticketList(request):    

    context={
        
    }
    return render(request,"taskmanagement/ticketList.html",context)