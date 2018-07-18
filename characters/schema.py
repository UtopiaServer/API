import graphene
from graphene_django import DjangoObjectType
from characters.types import CharacterType
from characters.models import Character


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
        character = Character(
            status=0,
            age=0,
            first_name=first_name,
            last_name=last_name
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
    characters = graphene.List(CharacterType)

    def resolve_characters(self, info, id=None, **kwargs):
        if id:
            filter = (
                Q(id=id)
            )
            return Character.objects.filter(filter)
        return Character.objects.all()


class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
