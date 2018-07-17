import graphene

import characters.schema
import inventories.schema
import players.schema
import worlds.schema
import launcher.schema


class Query(
            characters.schema.Query,
            inventories.schema.Query,
            players.schema.Query,
            worlds.schema.Query,
            launcher.schema.Query,
            graphene.ObjectType
        ):
    pass


class Mutation(
            characters.schema.Mutation,
            inventories.schema.Mutation,
            players.schema.Mutation,
            worlds.schema.Mutation,
            launcher.schema.Mutation,
            graphene.ObjectType
        ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
