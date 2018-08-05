import graphene

import characters.schema
import inventories.schema
import players.schema
import worlds.schema
import factions.schema
import territories.schema


class Query(
            characters.schema.Query,
            inventories.schema.Query,
            players.schema.Query,
            worlds.schema.Query,
            factions.schema.Query,
            territories.schema.Query,
            graphene.ObjectType
        ):
    pass


class Mutation(
            characters.schema.Mutation,
            inventories.schema.Mutation,
            players.schema.Mutation,
            worlds.schema.Mutation,
            factions.schema.Mutation,
            territories.schema.Mutation,
            graphene.ObjectType
        ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
