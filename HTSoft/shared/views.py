from django.shortcuts import render
from .models import Customer

# Create your views here.
def customerList(request):

    customers=Customer.objects.all().order_by('id')

    context={
        'customers':customers
    }

    return render(request,"shared/customerList.html",context)

