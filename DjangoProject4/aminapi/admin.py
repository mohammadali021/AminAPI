from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from aminapi.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile_number', 'phone_number', 'address' , 'lat' , 'lng')