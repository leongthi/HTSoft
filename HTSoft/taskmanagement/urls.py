from django.urls import path
from . import views

urlpatterns = [
    path("task_dashboard",views.task_dashboard,name="task_dashboard"),
    path("buildTickets/<int:BuildID>",views.buildTickets,name="buildTickets"),
    path("ticketList",views.ticketList,name="ticketList"),
    path("ticketWeekList/weekid=<int:weekid>&teamid=<int:teamid>/",views.ticketWeekList,name="ticketWeekList"),
]
