from django.contrib import admin
from .models import Employer, Hiring


@admin.register(Employer)
class EmployeeAdmin(admin.ModelAdmin):
    list_display  = ['organization_name','organization_contact','organization_email','organization_address']
    search_fields = ['organization_name','organization_contact','organization_email','organization_address']


@admin.register(Hiring)
class HiringAdmin(admin.ModelAdmin):
    list_display  = ['organization','hiring_manager','hiring_manager_email']
    search_fields = ['organization','hiring_manager','hiring_manager_email']
