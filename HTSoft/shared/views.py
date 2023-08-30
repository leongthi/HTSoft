from django.shortcuts import render
from .models import Customer,Client, UsersTicket
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

    clients=Client.objects.all().order_by('id')

    context={
        'clients':clients
    }

    return render(request,"shared/clientList.html",context)

def usersTicketList(request):

    usersTickets=UsersTicket.objects.all().order_by('UserID')

    # lst_user=ft.Initial(api.usersticket_getall())   
    # if lst_user is not None:
    #     for user in lst_user:
    #         if user is None:
    #             continue
    #         check_user=UsersTicket.objects.filter(UserID=user["ID"])
    #         if check_user:                
    #             continue
            
    #         else:
    #             UserID=user["ID"]
    #             Responsibility=user["Responsibility"]
    #             FirstName=user["FirstName"]
    #             LastName=user["LastName"]
    #             Email=user["Email"]
    #             PasswordEmail=user["PasswordEmail"]
    #             Tel=user["Tel"]
    #             ClientID=user["ClientID"]
    #             UserName=user["UserName"]
    #             PASSWORD=user["PASSWORD"]
    #             Skype=user["Skype"]
    #             IsActive=user["IsActive"]
    #             created_date=parser.isoparse(user["CreatedOn"]) if user["CreatedOn"] is not None else None
    #             modified_date=parser.isoparse(user["ModifiedOn"]) if user["ModifiedOn"] is not None else None
    #             created_by=user["CreatedBy"]
    #             modified_by=user["ModifiedBy"]
    #             NewID=user["NewID"]
                
    #             userTicket=UsersTicket(
    #                 UserID=UserID,
    #                 Responsibility=Responsibility,
    #                 FirstName=FirstName,
    #                 LastName=LastName,
    #                 Email=Email,
    #                 PasswordEmail=PasswordEmail,
    #                 Tel=Tel,
    #                 ClientID=ClientID,
    #                 UserName=UserName,
    #                 PASSWORD=PASSWORD,
    #                 Skype=Skype,
    #                 IsActive=IsActive,
    #                 created_date=created_date,
    #                 modified_date=modified_date,
    #                 created_by=created_by,
    #                 modified_by=modified_by,
    #                 NewID=NewID,
    #             )

    #             userTicket.save()

    context={
        'usersTickets':usersTickets
    }
    return render(request,"shared/usersTicketList.html",context)
