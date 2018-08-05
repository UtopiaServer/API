import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from factions.models import Faction
from factions.types import FactionType
from territories.models import Territory
from territories.types import TerritoryType
import itertools

class CreateTerritory(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    minX = graphene.Int()
    minY = graphene.Int()
    minZ = graphene.Int()
    maxX = graphene.Int()
    maxY = graphene.Int()
    maxZ = graphene.Int()
    dimension = graphene.Int()
    faction = graphene.Field(FactionType)

    class Arguments:
        name = graphene.String()
        minX = graphene.Int()
        minY = graphene.Int()
        minZ = graphene.Int()
        maxX = graphene.Int()
        maxY = graphene.Int()
        maxZ = graphene.Int()
        dimension = graphene.Int()
        factionID = graphene.Int()

    def mutate(self, info, name, minX, minY, minZ, maxX, maxY, maxZ, dimension, factionID):
        faction = Faction.objects.filter(id=factionID).first()
        if not faction:
            raise Exception("Invalid faction !")
        
        territory = Territory.objects.create(
            name=name,
            minX=minX,
            minY=minY,
            minZ=minZ,
            maxX=maxX,
            maxY=maxY,
            maxZ=maxX,
            dimension=dimension,
            faction=faction
        )

        return CreateTerritory(
            id=territory.id,
            name=territory.name,
            minX=territory.minX,
            minY=territory.minY,
            minZ=territory.minZ,
            maxX=territory.maxX,
            maxY=territory.maxY,
            maxZ=territory.maxX,
            dimension=territory.dimension,
            faction=territory.faction
        )

class DeleteTerritory(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        territory = Territory.objects.filter(id=id).first()

        if not territory:
            raise Exception("Territory not valid !")
        
        territory.delete()

        return DeleteTerritory(
            id=id
        )

class Query(graphene.ObjectType):
    territories = graphene.List(TerritoryType, id=graphene.Int(), name=graphene.String(), factionID=graphene.Int())

    def resolve_territories(self, info, id=None, name=None, factionID=None, **kwargs):
        territories = Territory.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            territories = territories.filter(filter)
        if factionID:
            faction = Faction.objects.all().filter(id=factionID).first()
            filter = (
                Q(faction=faction)
            )
            territories = territories.filter(filter)
        if name is not None and id is None:
            filter = (
                Q(name__startswith=name)
            )
            territories = territories.filter(filter)
        return territories


class Mutation(graphene.ObjectType):
    create_territory = CreateTerritory.Field()
    delete_territory = DeleteTerritory.Field()

