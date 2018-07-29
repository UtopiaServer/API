import graphene
from graphene_django import DjangoObjectType
from factions.models import Faction


class FactionType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Faction


