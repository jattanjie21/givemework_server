from graphene import ObjectType, String, Int, Field, Mutation,Boolean, List
from .models import *
from .query_types import *


# region seeker mutations
class CreateSeeker(Mutation):
    class Arguments:
        first_name    = String(required=True)
        middle_name   = String(required=False)
        last_name     = String(required=True)
        date_of_birth = String(required=True)
        email         = String(required=True)
        phone         = Int(required=True)

    seeker = Field(SeekerType)

    def mutate(self,info, first_name,middle_name,last_name,date_of_birth,email,phone):
        seeker = Seeker(
            first_name    = first_name,
            middle_name   = middle_name,
            last_name     = last_name,
            date_of_birth = date_of_birth,
            email         = email,
            phone         = phone
            )
        seeker.save()
        return CreateSeeker(seeker=seeker)


class UpdateSeeker(Mutation):
    class Arguments:
        id            = Int(required=True)
        first_name    = String(required=False)
        middle_name   = String(required=False)
        last_name     = String(required=False)
        date_of_birth = String(required=False)
        email         = String(required=False)
        phone         = Int(required=False)

    seeker = Field(SeekerType)

    def mutate(self,info, id, first_name,middle_name,last_name,date_of_birth,email,phone):
        seeker = Seeker.objects.get(id=id)

        seeker.first_name    = first_name
        seeker.middle_name   = middle_name
        seeker.last_name     = last_name
        seeker.date_of_birth = date_of_birth
        seeker.email         = email
        seeker.phone         = phone

        seeker.save()
        return UpdateSeeker(seeker=seeker)


class DeleteSeeker(Mutation):
    class Arguments:
        id = Int(required=True)

    seeker = Field(SeekerType)
    success = Boolean()

    def mutate(self,info, id):
        seeker = Seeker.objects.get(id=id)
        seeker.delete()
        return DeleteSeeker(seeker=seeker, success=True)
# endregion seeker mutations