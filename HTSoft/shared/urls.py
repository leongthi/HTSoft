from django.urls import path
from . import views

urlpatterns = [
    path("customerList",views.customerList,name="customerList"),
    path("clientList",views.clientList,name="clientList"),
]
