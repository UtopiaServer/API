import graphene
from graphene_django import DjangoObjectType
from players.models import PlayerPosition, Player, PlayerCharacter


class PlayerPositionType(DjangoObjectType):

    class Meta:
        model = PlayerPosition


class PlayerType(DjangoObjectType):

    class Meta:
        model = Player


class PlayerCharacterType(DjangoObjectType):
    class Meta:
        model = PlayerCharacter
