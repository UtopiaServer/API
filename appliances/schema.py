import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from appliances.models import Appliance
from appliances.types import ApplianceType
import itertools


class CreateAppliance(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    age = graphene.Int()
    country = graphene.String()
    way_of_known = graphene.Int()
    discord_handle = graphene.String()
    minecraft_username = graphene.String()
    have_you = graphene.String()
    gamemodes = graphene.String()
    expectations = graphene.String()
    appliance = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        age = graphene.Int()
        country = graphene.String()
        way_of_known = graphene.Int()
        discord_handle = graphene.String()
        minecraft_username = graphene.String()
        have_you = graphene.String()
        gamemodes = graphene.String()
        expectations = graphene.String()
        appliance = graphene.String()

    def mutate(self, info, first_name,
               last_name, age, country,
               way_of_known, discord_handle,
               minecraft_username, have_you,
               gamemodes, expectations, appliance):
        appliance = Appliance.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            country=country,
            way_of_known=way_of_known,
            discord_handle=discord_handle,
            minecraft_username=minecraft_username,
            have_you=have_you,
            gamemodes=gamemodes,
            expectations=expectations,
            appliance=appliance
        )

        return CreateAppliance(
            id=appliance.id,
            first_name=appliance.first_name,
            last_name=appliance.last_name,
            age=appliance.age,
            country=appliance.country,
            way_of_known=appliance.way_of_known,
            discord_handle=appliance.discord_handle,
            minecraft_username=appliance.minecraft_username,
            have_you=appliance.have_you,
            gamemodes=appliance.gamemodes,
            expectations=appliance.expectations,
            appliance=appliance.appliance
        )


class DeleteAppliance(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        appliance = Appliance.objects.filter(id=id).first()
        local_id = appliance.id
        appliance.delete()

        return DeleteAppliance(
            id=local_id,
        )


class Query(graphene.ObjectType):
    appliances = graphene.List(ApplianceType, id=graphene.Int())

    def resolve_appliances(self, info, id=None, **kwargs):
        appliances = Appliance.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            appliances = appliances.filter(filter)
        return appliances


class Mutation(graphene.ObjectType):
    create_appliance = CreateAppliance.Field()
    delete_appliance = DeleteAppliance.Field()

