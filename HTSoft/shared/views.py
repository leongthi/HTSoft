from django.shortcuts import render
from .models import Customer,Client

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