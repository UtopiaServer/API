from graphene_django import DjangoObjectType
from players.models import Player, PlayerCharacter


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class PlayerCharacterType(DjangoObjectType):
    class Meta:
        model = PlayerCharacter
