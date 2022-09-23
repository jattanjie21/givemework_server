from django.contrib import admin
from .models import JobCategories, JobSkillSet, Job


admin.site.register(JobCategories)


admin.site.register(JobSkillSet)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display  = ['job_title','created_by','recruitment_start_date','recruitment_end_date','recruitment_quota','location']
    search_fields = ['job_title','created_by','recruitment_quota','location']
