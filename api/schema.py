"""
UtopiaServer API ~ All Right reserved.

Main schema for the API.
"""

import graphene
import graphql_jwt

from characters.schema import Query as CharacterQuery
from characters.schema import Mutation as CharacterMutation

from inventories.schema import Query as InventoryQuery
from inventories.schema import Mutation as InventoryMutation

from players.schema import Query as PlayerQuery
from players.schema import Mutation as PlayerMutation

from worlds.schema import Query as WorldQuery
from worlds.schema import Mutation as WorldMutation

from factions.schema import Query as FactionQuery
from factions.schema import Mutation as FactionMutation

from territories.schema import Query as TerritoryQuery
from territories.schema import Mutation as TerritoryMutation

from launcher.schema import Query as LauncherQuery
from launcher.schema import Mutation as LauncherMutation

from appliances.schema import Query as ApplianceQuery
from appliances.schema import Mutation as ApplianceMutation


class Query(
        CharacterQuery,
        InventoryQuery,
        PlayerQuery,
        WorldQuery,
        FactionQuery,
        TerritoryQuery,
        LauncherQuery,
        ApplianceQuery,
        graphene.ObjectType
):
    """Query class for the GraphQL interface."""


class Mutation(
        CharacterMutation,
        InventoryMutation,
        PlayerMutation,
        WorldMutation,
        FactionMutation,
        TerritoryMutation,
        LauncherMutation,
        ApplianceMutation,
        graphene.ObjectType
):
    """Mutation class for the GraphQL interface."""

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)
