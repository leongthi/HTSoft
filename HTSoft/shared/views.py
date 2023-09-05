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

    #Get clients list
    clients=ft.Initial(api.clients_getall())


    context={
        'clients':clients
    }

    return render(request,"shared/clientList.html",context)


def usersTicketList(request):
    usersTicket=ft.Initial(api.usersTicket_getall())

    context={
        'usersTicket':usersTicket
    }

    return render(request,"shared/usersTicketList.html",context)

