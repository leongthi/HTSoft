from django.urls import path
from . import views

urlpatterns = [
    path("folderList",views.folderList,name="folderList"),
]
