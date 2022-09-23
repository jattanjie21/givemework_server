from django.db import models
from utilities.models import Individual,TimeStamp
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


class Seeker(Individual):
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'Seeker'


class Education(TimeStamp):
    start_date    = models.DateField(verbose_name='Start Date')
    end_date      = models.DateField(verbose_name='End Date')
    institution   = models.CharField(max_length=255)
    certification = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.institution

    class Meta:
        verbose_name_plural = 'Education'


class Skills(TimeStamp):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Skills'


class Experience(TimeStamp):
    start_date  = models.DateField(verbose_name='Start Date')
    end_date    = models.DateField(verbose_name='End Date')
    company     = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name_plural = 'Experience'


class SeekerProfile(TimeStamp):
    seeker     = models.OneToOneField(Seeker, on_delete=models.CASCADE)
    education  = models.ManyToManyField(Education)
    experience = models.ManyToManyField(Experience)
    skills     = models.ManyToManyField(Skills)

    def __str__(self):
        return self.seeker.email

    class Meta:
        verbose_name_plural = 'Seeker Profile'

    @receiver(post_save, sender=Seeker)
    def create_seeker_profile_after_a_seeker_is_created(sender, instance, created, **kwargs):
        try:
            if created:
                SeekerProfile.objects.create(seeker=instance)
        except:
            return Exception('Seeker Profile was not created')

    @receiver(post_delete, sender=Seeker)
    def delete_seeker_profile_after_a_seeker_is_deleted(sender, instance, **kwargs):
        try:
            instance.seekerprofile.delete()
        except:
            return Exception('Seeker Profile was not deleted')