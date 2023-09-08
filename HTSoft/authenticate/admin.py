from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('map_user_ticket','avatar')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Information', {'fields': ('map_user_ticket', 'avatar')}),
    )

    def save_model(self, request, obj, form, change):
        if form.cleaned_data['map_user_ticket'] is None:
            raise ValueError("Your field must have a value.")
        obj.map_user_ticket = form.cleaned_data['map_user_ticket'].id
        super().save_model(request, obj, form, change)
    

admin.site.register(CustomUser, CustomUserAdmin)