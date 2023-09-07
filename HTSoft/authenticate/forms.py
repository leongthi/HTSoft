from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['map_user_ticket'].initial = self.instance.map_user_ticket
        


