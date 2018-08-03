import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from factions.models import Faction, Membership
from factions.types import FactionType
from characters.types import CharacterType
from characters.models import Character
import itertools

class CreateFaction(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        faction = Faction.objects.create(
            name=name
        )

        return CreateFaction(
            id=faction.id,
            name=faction.name
        )


class DeleteFaction(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        faction = Faction.objects.filter(id=id).first()
        local_id = faction.id
        local_name = faction.name
        faction.delete()

        return CreateFaction(
            id=local_id,
            name=local_name
        )

class InviteCharacter(graphene.Mutation):
    faction = graphene.Field(FactionType)
    character = graphene.Field(CharacterType)

    class Arguments:
        faction_id = graphene.Int()
        character_id = graphene.Int()
        inviter_id = graphene.Int()

    def mutate(self, info, faction_id, character_id, inviter_id):
        character = Character.objects.filter(id=character_id).first()

        if not character:
            raise Exception("Invalid character !")

        inviter = Character.objects.filter(id=inviter_id).first()

        if not inviter:
            raise Exception("Invalid inviter !")

        faction = Faction.objects.filter(id=faction_id).first()

        if not faction:
            raise Exception("Invalid faction !")

        membership = Membership.objects.create(
            faction=faction,
            character=character,
            inviter=inviter
        )
        membership.save()

        return InviteCharacter(
            faction=faction,
            character=character 
        )

class KickCharacter(graphene.Mutation):
    faction = graphene.Field(FactionType)
    character = graphene.Field(CharacterType)

    class Arguments:
        faction_id = graphene.Int()
        character_id = graphene.Int()

    def mutate(self, info, faction_id, character_id):
        character = Character.objects.filter(id=character_id).first()

        if not character:
            raise Exception("Invalid character !")

        faction = Faction.objects.filter(id=faction_id).first()

        if not faction:
            raise Exception("Invalid faction !")

        membership = Membership.objects.filter(
            faction=faction,
            character=character
        )
        if membership is not None:
            membership.delete()
        else:
            raise Exception("Membership not found.")

        return KickCharacter(
            faction=faction,
            character=character 
        )

class Query(graphene.ObjectType):
    factions = graphene.List(FactionType, id=graphene.Int(), name=graphene.String())

    def resolve_factions(self, info, id=None, name=None, **kwargs):
        factions = Faction.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            factions = factions.filter(filter)
        if name is not None and id is None:
            filter = (
                Q(name__startswith=name)
            )
            factions = factions.filter(filter)
        return factions


class Mutation(graphene.ObjectType):
    create_faction = CreateFaction.Field()
    delete_faction = DeleteFaction.Field()
    invite_character = InviteCharacter.Field()
    kick_character = KickCharacter.Field()

