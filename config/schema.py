from graphene import ObjectType
from core.seeker.schema import SeekerQuery, SeekerMutation

class Query(ObjectType):
    hello = graphene.String(default_value="Hi!")


class Mutation(SeekerMutation,ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)