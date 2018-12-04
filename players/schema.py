import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from characters.types import CharacterType
from characters.models import Character
from players.types import PlayerType, PlayerCharacterType
from players.models import PlayerPosition, Player, PlayerCharacter


class Query(graphene.ObjectType):
    player = graphene.Field(PlayerType, uuid=graphene.UUID())
    players = graphene.List(PlayerType)

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_player(self, info, uuid=None, **kwargs):
        filter = (
            Q(uuid=uuid)
        )
        return Player.objects.filter(filter).first()
        



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

class MovePlayer(graphene.Mutation):
    
    player = graphene.Field(PlayerType)

    class Arguments:
        uuid = graphene.UUID()
        x = graphene.Integer()
        y = graphene.Integer()
        z = graphene.Integer()
        dim = graphene.Integer()
    
    def mutate(self, info, uuid, x, y, z, dim):
        player = Player.objects.filter(uuid=uuid).first()

        if not player:
            raise Exception("Invalid player")

        if not player.position:
            player.position = PlayerPosition.objects.create(
                x=x,
                y=y,
                z=z,
                dim=dim
            )
        
        player.position.x = x
        player.position.y = y
        player.position.z = z
        player.position.dim = dim
        player.position.save()
        player.save()

        return MovePlayer(
            player=player
        )

class Mutation(graphene.ObjectType):
    create_player = CreatePlayer.Field()
    associate_player_character = AssociatePlayerCharacter.Field()
    move_player = MovePlayer.Field()
