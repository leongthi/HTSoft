from django.shortcuts import render

# Create your views here.
def customerList(request):
    context={

    }

    return render(request,"shared/customerList.html",context)