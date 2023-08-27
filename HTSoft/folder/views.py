from django.shortcuts import render

# Create your views here.
def folderList(request):
    context={

    }
    return render(request,"folder/folderList.html",context)