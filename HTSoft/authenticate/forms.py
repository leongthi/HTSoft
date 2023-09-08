from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from shared.models import UserTicket


class CustomUserChangeForm(UserChangeForm):
    map_user_ticket = forms.ModelChoiceField(queryset=UserTicket.objects.all())
    class Meta(UserChangeForm.Meta):
        model = CustomUser


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'map_user_ticket' in self.fields:
            self.fields['map_user_ticket'].initial = self.instance.map_user_ticket

class CustomUserCreationForm(UserCreationForm):
    map_user_ticket = forms.ModelChoiceField(queryset=UserTicket.objects.all())
    class Meta(UserCreationForm.Meta):
        model = CustomUser


