from graphene_django import DjangoObjectType
from seeker.models import *
from employer.models import *


class SeekerType(DjangoObjectType):
    class Meta:
        model = Seeker


class EducationType(DjangoObjectType):
    class Meta:
        model = Education


class SkillsType(DjangoObjectType):
    class Meta:
        model = Skills


class ExperienceType(DjangoObjectType):
    class Meta:
        model = Experience


class SeekerProfileType(DjangoObjectType):
    class Meta:
        model = SeekerProfile


class EmployerType(DjangoObjectType):
    class Meta:
        model = Employer


class HiringType(DjangoObjectType):
    class Meta:
        model = Hiring