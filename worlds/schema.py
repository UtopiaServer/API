import graphene
from graphene_django import DjangoObjectType

from .models import World


class WorldType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = World


class Query(graphene.ObjectType):
    worlds = graphene.List(WorldType)

    def resolve_worlds(self, info, **kwargs):
        return World.objects.all()


class CreateWorld(graphene.Mutation):
    world = graphene.Field(WorldType)

    class Arguments:
        name = graphene.String()
        ip = graphene.String()
        port = graphene.Int()

    def mutate(self, info, name, ip, port):
        world = World(
            name=name,
            ip=ip,
            port=port,
            state=True
        )
        world.save()

        return CreateWorld(
            world=world
        )


class SetWorldState(graphene.Mutation):
    world = graphene.Field(WorldType)

    class Arguments:
        world_id = graphene.Int()
        state = graphene.Boolean()
    
    def mutate(self, info, world_id, state):
        world = World.objects.filter(id=world_id).first()

        if not world:
            raise Exception("Invalid World !")

        world.state = state
        world.save()

        return SetWorldState(
            world=world
        )


class Mutation(graphene.ObjectType):
    create_world = CreateWorld.Field()
    set_world_state = SetWorldState.Field()
