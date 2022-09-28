from graphene import List, Field, Int, String, Boolean, ObjectType
from .all_query_types import *
from .all_mutations import *
from seeker.models import *
from employer.models import *
from jobs.models import *

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


    # get all employees list
    all_employers = List(EmployerType)

    def resolve_all_employers(self, info, **kwargs):
        return Employer.objects.all()

    # get employer by id
    employer = Field(EmployerType, id=Int())

    def resolve_employer(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Employer.objects.get(pk=id)

        return None

    # get all employers list in a particular address
    all_employers_in_address = List(EmployerType, organization_address=String())

    def resolve_all_employers_in_address(self, info, **kwargs):
        organization_address = kwargs.get('organization_address')

        if organization_address is not None:
            return Employer.objects.filter(organization_address=organization_address)

        return None


class Mutation(ObjectType):
    create_seeker = CreateSeeker.Field()
    update_seeker = UpdateSeeker.Field()
    delete_seeker = DeleteSeeker.Field()

    create_employer = CreateEmployer.Field()
    update_employer = UpdateEmployer.Field()
    delete_employer = DeleteEmployer.Field()