import graphene
from graphene_django import DjangoObjectType
from characters.schema import Character
from characters.schema import CharacterType
from .models import Inventory, ItemStack


class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory


class ItemStackType(DjangoObjectType):
    class Meta:
        model = ItemStack


class Query(graphene.ObjectType):
    inventories = graphene.List(InventoryType)
    item_stacks = graphene.List(ItemStackType)

    def resolve_inventories(self, info, **kwargs):
        return Inventory.objects.all()

    def resolve_item_stacks(self, info, **kwargs):
        return ItemStack.objects.all()


class CreateInventory(graphene.Mutation):
    id = graphene.Int()
    character = graphene.Field(CharacterType)

    class Arguments:
        character_id = graphene.Int()

    def mutate(self, info, character_id):
        character = Character.objects.filter(id=character_id).first()

        if not character:
            raise Exception('Invalid Character!')

        Inventory.objects.create(
            character=character
        )

        return CreateInventory(
            character=character
        )


class CreateItemStack(graphene.Mutation):
    inventory = graphene.Field(InventoryType)
    registry_name = graphene.String()
    count = graphene.Int()
    nbt_data = graphene.String()

    class Arguments:
        inventory_id = graphene.Int()
        registry_name = graphene.String()
        count = graphene.Int()
        nbt_data = graphene.String()

    def mutate(self, info, inventory_id, registry_name, count, nbt_data):
        inventory = Inventory.objects.filter(character_id=inventory_id).first()

        if not inventory:
            raise Exception('Invalid Inventory!')

        ItemStack.objects.create(
            inventory=inventory,
            registry_name=registry_name,
            count=count,
            nbt_data=nbt_data
        )

        return CreateItemStack(
            inventory=inventory,
            registry_name=registry_name,
            count=count,
            nbt_data=nbt_data
        )


#4
class Mutation(graphene.ObjectType):
    create_inventory = CreateInventory.Field()
    create_itemstack = CreateItemStack.Field()