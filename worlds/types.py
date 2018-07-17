import graphene
from graphene_django import DjangoObjectType
from worlds.models import World


class WorldType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = World

