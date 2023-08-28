from django.shortcuts import render,get_object_or_404,redirect
from .models import Build
from shared.models import Customer, Status

# Create your views here.
def task_dashboard(request):

    builds=Build.objects.all().order_by('id')


    context={
        'builds':builds
    }
    return render(request,"taskmanagement/task_dashboard.html",context)

def task_dashboard_buildUpdate(request,id):

    build=get_object_or_404(Build,pk=id)
    if build is None:
        return
    

    if request.method=='POST':
        BuildName=request.POST.get('BuildName')
        BuildCustomerID=request.POST.get('BuildCustomerID')
        BuildStatusID=request.POST.get('BuildStatusID')
        BuildDeadline=request.POST.get('BuildDeadline')
        created_by=request.user
        modified_by=request.user


        build.BuildName=BuildName
        build.BuildCustomerID=BuildCustomerID
        build.BuildStatusID=BuildStatusID
        build.BuildDeadline=BuildDeadline
        build.created_by=created_by
        build.modified_by=modified_by

        build.save()
        return redirect('task_dashboard')
    