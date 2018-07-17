import graphene
from graphene_django import DjangoObjectType
from characters.models import Character


class CharacterType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Character
