from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _
from app1.models import CustomUser
from app1.forms import CustomUserChangeForm, CustomUserCreationForm

from .models import *
from .forms import *

# Register your models here.

class TrafficFineAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "full_name", "offence", "amount", "status"]
    form = PublicTrafficForm

admin.site.register(TrafficFine, TrafficFineAdmin) 


class FIRAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "full_name", "timestamp", "complaint", "status"]
    form = FIRForm

admin.site.register(FIR, FIRAdmin) 


class ContactAdmin(admin.ModelAdmin):
    list_display = ["timestamp", "full_name", "email", "rank", "badge_no", "message", "read_status"]
    form = ContactForm

admin.site.register(Message, ContactAdmin)



class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'rank', 'badge_no')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'rank', 'badge_no', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)







