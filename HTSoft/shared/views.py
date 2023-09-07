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


    if not usertk_db:
        for utk in usersTicket:
            user=UserTicket(
                ID_main=utk["ID"],
                UserName=utk["UserName"],
                PASSWORD=utk["PASSWORD"],
                Responsibility=utk["Responsibility"],
                FirstName=utk["FirstName"],
                Email=utk["Email"],
                IsActive=utk["IsActive"],
            )

            user.save()
        context={
            'usertk_db':usertk_db
        }

        return render(request,"shared/usersTicketList.html",context)
    else:
        for utk in usersTicket:        
            for us_db in usertk_db:                
                if  us_db.UserName==utk["UserName"]:
                    if utk["UserName"] != us_db.UserName or utk["PASSWORD"] != us_db.PASSWORD  or utk["Responsibility"] != us_db.Responsibility or utk["FirstName"] != us_db.FirstName or utk["Email"] != us_db.Email or utk["IsActive"] != us_db.IsActive:
                        us_db.ID_main=utk["ID"]
                        us_db.UserName=utk["UserName"]
                        us_db.PASSWORD=utk["PASSWORD"]
                        us_db.Responsibility=utk["Responsibility"]
                        us_db.FirstName=utk["FirstName"]
                        us_db.Email=utk["Email"]
                        us_db.IsActive=utk["IsActive"]

                        us_db.save()

                else:
                    continue             

        context={
            'usertk_db':usertk_db
        }

        return render(request,"shared/usersTicketList.html",context)

