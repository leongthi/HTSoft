from django.shortcuts import render
from shared.models import Customer

# Create your views here.
def folderList(request):

    customers=Customer.objects.all().order_by('id')

    context={
        'customers':customers
    }
    return render(request,"folder/folderList.html",context)