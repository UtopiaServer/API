from django.contrib import admin
from .models import Inventory, ItemStack
# Register your models here.

admin.site.register(Inventory)
admin.site.register(ItemStack)
