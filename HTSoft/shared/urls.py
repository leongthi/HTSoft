from django.urls import path
from . import views

urlpatterns = [
    path("clientList",views.clientList,name="clientList"),
    path("usersTicketList",views.usersTicketList,name="usersTicketList"),
    path("clientEdit/<int:id>",views.clientEdit,name="clientEdit"),
]
