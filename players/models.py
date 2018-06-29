from django.db import models
from characters.models import Character

# Create your models here.


class Player(models.Model):

    uuid = models.UUIDField(primary_key=True)


class PlayerCharacter(models.Model):

    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        primary_key=True
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
