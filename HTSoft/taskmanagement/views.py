from django.shortcuts import render,get_object_or_404,redirect
from .models import Build
from shared.models import Customer, Status
from . import api
from . import functions as ft

from dateutil import parser

# Create your views here.
def task_dashboard(request):
    builds=Build.objects.all().order_by('id')    


    lst_build=ft.InitialBuild(api.builds_getall())    
    if lst_build is not None:
        for build in lst_build:

            check_build=Build.objects.filter(BuildID=build["BuildID"])

            if check_build is not None:
                continue
            
            else:
                BuildID=build["BuildID"]
                ClientID=build["ClientID"]
                BuildName=build["BuildName"]
                BuildStatus=build["Status"]
                BuildDeadline=parser.isoparse(build["DueDate"])
                
                b=Build(
                    BuildID=BuildID,
                    ClientID=ClientID,
                    BuildName=BuildName,
                    BuildStatus=BuildStatus,
                    BuildDeadline=BuildDeadline
                )

                b.save()
    context={
        'builds':builds
    }
    return render(request,"taskmanagement/task_dashboard.html",context)

def task_dashboard_buildUpdate(request,id):

    build=get_object_or_404(Build,pk=id)
    if build is None:
        return
    
    

def buildTickets(request,BuildID):
    
    context={

    }
    return render(request,"taskmanagement/buildTickets.html",context)
    