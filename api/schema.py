import graphene
import graphql_jwt
import characters.schema
import inventories.schema
import players.schema
import worlds.schema
import factions.schema
import territories.schema
import launcher.schema


class Query(
            characters.schema.Query,
            inventories.schema.Query,
            players.schema.Query,
            worlds.schema.Query,
            factions.schema.Query,
            territories.schema.Query,
            launcher.schema.Query,
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
            launcher.schema.Mutation,
            graphene.ObjectType
        ):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
