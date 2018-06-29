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
    slot = graphene.Int()

    class Arguments:
        inventory_id = graphene.Int()
        registry_name = graphene.String()
        count = graphene.Int()
        nbt_data = graphene.String()
        slot = graphene.Int()

    def mutate(self, info, inventory_id, registry_name, count, nbt_data, slot):
        inventory = Inventory.objects.filter(character_id=inventory_id).first()

        if not inventory:
            raise Exception('Invalid Inventory!')

        ItemStack.objects.create(
            inventory=inventory,
            registry_name=registry_name,
            count=count,
            nbt_data=nbt_data,
            slot=slot
        )

        return CreateItemStack(
            inventory=inventory,
            registry_name=registry_name,
            count=count,
            nbt_data=nbt_data,
            slot=slot
        )


class CleanInventory(graphene.Mutation):
    inventory = graphene.Field(InventoryType)

    class Arguments:
        inventory_id = graphene.Int()

    def mutate(self, info, inventory_id):
        inventory = Inventory.objects.filter(character_id=inventory_id).first()

        if not inventory:
            raise Exception("Invalid Inventory !")

        ItemStack.objects.filter(inventory=inventory).delete()

        return CleanInventory(
            inventory=inventory
        )


class Mutation(graphene.ObjectType):
    create_inventory = CreateInventory.Field()
    create_itemstack = CreateItemStack.Field()
    clean_inventory = CleanInventory.Field()
