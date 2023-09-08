from django.shortcuts import render
from shared.models import Client


# Create your views here.
def folderList(request):

    clients=Client.objects.all().filter(ActiveYN=1).order_by('id')

    context={
        'clients':clients
    }
    return render(request,"folder/folderList.html",context)