import graphene

import characters.schema
import inventories.schema

class Query(characters.schema.Query, inventories.schema.Query, graphene.ObjectType):
    pass

class Mutation(characters.schema.Mutation, inventories.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
