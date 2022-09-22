from graphene_django import DjangoObjectType
from .models import *


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