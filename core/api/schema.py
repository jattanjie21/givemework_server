from seeker.mutations import *
from graphene import List, Field, Int, String, Boolean, ObjectType
from .all_query_types import *
from .all_mutations import *

class Query(ObjectType):

    # get list of all seekers
    all_seekers = List(SeekerType)

    def resolve_all_seekers(self, info, **kwargs):
        return Seeker.objects.all()

    # get seeker by id
    seeker = Field(SeekerType, id=Int())

    def resolve_seeker(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Seeker.objects.get(pk=id)

        return None

    # get seeker by email
    seeker_by_email = Field(SeekerType, email=String())

    def resolve_seeker_by_email(self, info, **kwargs):
        email = kwargs.get('email')

        if email is not None:
            return Seeker.objects.get(email=email)

        return None


class Mutation(ObjectType):
    create_seeker = CreateSeeker.Field()
    update_seeker = UpdateSeeker.Field()
    delete_seeker = DeleteSeeker.Field()