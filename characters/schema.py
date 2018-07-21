import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from characters.types import CharacterType
from characters.models import Character
from players.types import PlayerType
from utils.random_name import FantasyNameGenerator
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
        if not len(first_name) or not len(last_name):
            names = [i for i in itertools.islice(FantasyNameGenerator(2, 10), 2)]
        character = Character(
            status=0,
            age=0,
            first_name=first_name if len(first_name) else names.pop(),
            last_name=last_name if len(last_name) else names.pop()
        )
        character.save()

        return CreateCharacter(
            id=character.id,
            status=character.status,
            age=character.age,
            first_name=character.first_name,
            last_name=character.last_name
        )


class Query(graphene.ObjectType):
    characters = graphene.List(CharacterType, id=graphene.Int(), player=graphene.Boolean())

    def resolve_characters(self, info, id=None, player=None, **kwargs):
        characters = Character.objects.all()
        if id:
            filter = (
                Q(id=id)
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


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
