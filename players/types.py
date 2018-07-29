import graphene
from graphene_django import DjangoObjectType
from players.models import Player, PlayerCharacter


class PlayerType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Player


class PlayerCharacterType(DjangoObjectType):
    class Meta:
        model = PlayerCharacter
