from .mutations import *
from graphene_django import Mutation,Query


class SeekerQuery(Query):
    pass


class SeekerMutation(Mutation):
    create_seeker = CreateSeeker.Field()
    update_seeker = UpdateSeeker.Field()
    delete_seeker = DeleteSeeker.Field()