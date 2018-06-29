import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from characters.schema import CharacterType
from characters.models import Character
from .models import Player, PlayerCharacter


class PlayerType(DjangoObjectType):
    class Meta:
        model = Player


class PlayerCharacterType(DjangoObjectType):
    class Meta:
        model = PlayerCharacter


class Query(graphene.ObjectType):
    players = graphene.List(PlayerType, uuid=graphene.UUID())

    def resolve_players(self, info, uuid=None, **kwargs):
        if uuid:
            filter = (
                Q(uuid=uuid)
            )
            return Player.objects.filter(filter)

        return Player.objects.all()


class CreatePlayer(graphene.Mutation):
    uuid = graphene.UUID()

    class Arguments:
        uuid = graphene.UUID()

    def mutate(self, info, uuid):
        Player.objects.create(
            uuid=uuid
        )

        return CreatePlayer(
            uuid=uuid
        )


class AssociatePlayerCharacter(graphene.Mutation):

    player = graphene.Field(PlayerType)
    character = graphene.Field(CharacterType)

    class Arguments:
        uuid = graphene.UUID()
        character_id = graphene.Int()

    def mutate(self, info, uuid, character_id):
        character = Character.objects.filter(id=character_id).first()

        if not character:
            raise Exception("Invalid character !")

        player = Player.objects.filter(uuid=uuid).first()

        if not player:
            raise Exception("Invalid player !")

        PlayerCharacter.objects.create(
            character=character,
            player=player
        )

        return AssociatePlayerCharacter(
            player=player,
            character=character
        )


class Mutation(graphene.ObjectType):
    create_player = CreatePlayer.Field()
    associate_player_character = AssociatePlayerCharacter.Field()
