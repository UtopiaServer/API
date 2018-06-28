from django.db import models
from characters.models import Character

# Create your models here.


class Inventory(models.Model):
    
    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self):
        return "{0} {1}'s inventory.".format(
            self.character.first_name,
            self.character.last_name
        )


class ItemStack(models.Model):

    registry_name = models.TextField(default="")
    count = models.IntegerField(default=0)
    nbt_data = models.TextField(default="{}")
    slot = models.CharField(max_length=20)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)

