from django.db import models
from utilities.models import TimeStamp
from employer.models import Hiring
from seeker.models import Seeker


class JobCategories(TimeStamp):
    category_name = models.CharField(max_length=200, verbose_name='Category Name')
    description   = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Job Categories'


class JobSkillSet(TimeStamp):
    skill_name = models.CharField(max_length=255, verbose_name='Skill Name')

    def __str__(self):
        return self.skill_name

    class Meta:
        verbose_name_plural = 'Job Skill Set'


class Job(TimeStamp):
    job_title              = models.CharField(max_length=255, verbose_name='Job Title')
    job_description        = models.TextField(verbose_name='Job Description')
    created_by             = models.OneToOneField(Hiring, on_delete=models.DO_NOTHING, verbose_name='Job Created By')
    skill_set              = models.ManyToManyField(JobSkillSet, verbose_name='Job Skill Sets')
    recruitment_start_date = models.DateField(verbose_name='Recruitment Start Date')
    recruitment_end_date   = models.DateField(verbose_name='Recruitment End Date')
    recruitment_quota      = models.CharField(max_length=255, verbose_name='Recruitment Quota')
    location               = models.CharField(max_length=255)

    def __str__(self):
        return self.job_title