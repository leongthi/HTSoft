from django.shortcuts import render
from .models import Customer
from . import api
from . import functions as ft
from dateutil import parser

# Create your views here.
def customerList(request):

    customers=Customer.objects.all().order_by('id')

    context={
        'customers':customers
    }

    return render(request,"shared/customerList.html",context)


def clientList(request):   

    context={
        
    }

    return render(request,"shared/clientList.html",context)

def usersTicketList(request):    

    usersTickets=ft.Initial(api.usersticket_getall())

    context={
        'usersTickets':usersTickets
    }
    return render(request,"shared/usersTicketList.html",context)
