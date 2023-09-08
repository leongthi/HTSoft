from django.shortcuts import render,get_object_or_404,redirect
from .models import UserTicket,Client
from . import api
from . import functions as ft


# Create your views here.

def clientList(request):   

    #Get clients list
    clients=ft.Initial(api.clients_getall())

    clients_db=Client.objects.all()

    if not clients_db:
        for cli in clients:
            client=Client(
                ID_main=cli["ID"],
                Code=cli["Code"],
                Name=cli["Name"],
                Status=cli["Status"],
                WebServiceURL=cli["WebServiceURL"],
                ActiveYN=cli["ActiveYN"]
            )

            client.save()
        context={
            'clients_db':clients_db
        }

        return render(request,"shared/clientList.html",context)
    else:
        for cli in clients:        
            for cli_db in clients_db:                
                if  cli_db.ID_main==cli["ID"]:
                    if cli["Code"] != cli_db.Code or cli["Name"] != cli_db.Name  or cli["Status"] != cli_db.Status or cli["WebServiceURL"] != cli_db.WebServiceURL or cli["ActiveYN"] != cli_db.ActiveYN:
                        cli_db.ID_main=cli["ID"]
                        cli_db.Code=cli["Code"]
                        cli_db.Name=cli["Name"]
                        cli_db.Status=cli["Status"]
                        cli_db.WebServiceURL=cli["WebServiceURL"]
                        cli_db.ActiveYN=cli["ActiveYN"]


                        cli_db.save()

                else:
                    continue             

        context={
            'clients_db':clients_db
        }

        return render(request,"shared/clientList.html",context)
    
def clientEdit(request,id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        Logo = request.FILES.get('Logo')
        print(Logo)
        if Logo:
            client.Logo = Logo

            client.save()
            return redirect('clientList')
    context = {
        'client': client,
    }
    return render(request, 'shared/clientEdit.html', context)


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
    


