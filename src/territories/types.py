from graphene_django import DjangoObjectType
from territories.models import Territory
import graphene


class TerritoryType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Territory


