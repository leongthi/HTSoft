from django.urls import path
from . import views

urlpatterns = [
    path("task_dashboard",views.task_dashboard,name="task_dashboard"),
    path("task_dashboard_buildUpdate/<int:id>",views.task_dashboard_buildUpdate,name="task_dashboard_buildUpdate"),
    path("buildTickets/<int:BuildID>",views.buildTickets,name="buildTickets"),
]
