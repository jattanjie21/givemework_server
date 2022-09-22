from django.contrib import admin
from .models import *


@admin.register(Seeker)
class SeekerAdmin(admin.ModelAdmin):
    list_display  = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'email_verified']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'email_verified']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'institution', 'certification']


admin.site.register(Skills)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'end_date', 'company', 'description']


admin.site.register(SeekerProfile)