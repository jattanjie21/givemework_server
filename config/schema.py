from graphene import ObjectType
from graphene import Schema, String
from core.api.schema import Query,Mutation

class Query(Query,ObjectType):
    pass


class Mutation(Mutation,ObjectType):
    pass


schema = Schema(query=Query,mutation=Mutation)