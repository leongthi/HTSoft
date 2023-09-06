from django.shortcuts import render
from .models import UserTicket
from . import api
from . import functions as ft
from dateutil import parser

# Create your views here.
def customerList(request):

    context={
        
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
    usertk_db=UserTicket.objects.all()

    if usertk_db is None:
        return

    context={
        'usersTicket':usersTicket
    }

    return render(request,"shared/usersTicketList.html",context)

