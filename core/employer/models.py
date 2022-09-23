from django.db import models
from utilities.models import TimeStamp


class Employer(TimeStamp):
    organization_name    = models.CharField(max_length=255)
    organization_contact = models.IntegerField(unique=True)
    organization_email   = models.EmailField(unique=True)
    organization_address = models.CharField(max_length=255)

    def __str__(self):
        return self.organization_name

    class Meta:
        verbose_name_plural = 'Employers'


class Hiring(TimeStamp):
    organization         = models.ForeignKey(Employer, on_delete=models.DO_NOTHING)
    hiring_manager       = models.CharField(max_length=255)
    hiring_manager_email = models.EmailField()

    def __str__(self):
        return str(self.organization)

    class Meta:
        verbose_name_plural = 'Hiring'