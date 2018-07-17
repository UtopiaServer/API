from graphene_django import DjangoObjectType
from inventories.models import Inventory, ItemStack


class InventoryType(DjangoObjectType):
    class Meta:
        model = Inventory


class ItemStackType(DjangoObjectType):
    class Meta:
        model = ItemStack

