import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from characters.types import CharacterType
from characters.models import Character
from players.types import PlayerType
from utils.namegen import MName
import itertools

class CreateCharacter(graphene.Mutation):
    id = graphene.Int()
    status = graphene.Int()
    age = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, first_name, last_name):
        names = []
        character = Character(
            status=0,
            age=0,
            first_name=first_name if len(first_name) else MName("utils/firstname.txt").New(),
            last_name=last_name if len(last_name) else MName("utils/surname.txt").New()
        )
        character.save()

        return CreateCharacter(
            id=character.id,
            status=character.status,
            age=character.age,
            first_name=character.first_name,
            last_name=character.last_name
        )


class CharacterIsDead(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        character = Character.objects.filter(id=id).first()
        character.status = 1
        character.playercharacter.delete()
        character.save()

        return CharacterIsDead(
            id=character.id
        )


class Query(graphene.ObjectType):
    characters = graphene.List(
        CharacterType,
        id=graphene.Int(),
        player=graphene.Boolean(),
        alive=graphene.Boolean()
    )

    character = graphene.Field(CharacterType, id=graphene.Int())

    def resolve_characters(self, info, id=None, player=None, alive=None, **kwargs):
        characters = Character.objects.all()
        if alive is not None and alive:
            filter = (
                Q(status=0)
            )
            characters = characters.filter(filter)
        if alive is not None and not alive:
            filter = (
                Q(status=1)
            )
            characters = characters.filter(filter)
        if player is not None and not player:
            filter = (
                Q(playercharacter=None)
            )
            characters = characters.filter(filter)
        if player is not None and player:
            filter = (
                Q(playercharacter=None)
            )
            characters = characters.exclude(filter)
        return characters

    def resolve_character(self, info, id=None):
        characters = Character.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            characters = characters.filter(filter)
        return characters.first()


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    character_is_dead = CharacterIsDead.Field()
