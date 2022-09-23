from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Individual(TimeStamp):
    first_name    = models.CharField(max_length=255)
    middle_name   = models.CharField(max_length=255, blank=True, null=True)
    last_name     = models.CharField(max_length=255)
    date_of_birth = models.DateField(verbose_name='Date of Birth')
    email         = models.EmailField()
    phone         = models.IntegerField()


    class Meta:
        abstract = True


class Location(models.Model):
    region    = models.CharField(max_length=100,blank=True,null=True)
    town      = models.CharField(max_length=100,blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    latitude  = models.FloatField(blank=True,null=True)
    address   = models.CharField(max_length=100)
    country   = models.CharField(max_length=200,default='Gambia')

    class Meta:
        abstract = True
