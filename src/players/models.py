from django.db import models
from characters.models import Character

# Create your models here.


class PlayerPosition(models.Model):
    """Define a player position."""

    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    dim = models.IntegerField()


class Player(models.Model):

    uuid = models.UUIDField(primary_key=True)
    position = models.OneToOneField(PlayerPosition, on_delete=models.CASCADE, null=True)


class PlayerCharacter(models.Model):

    character = models.OneToOneField(
        Character,
        on_delete=models.CASCADE,
        primary_key=True
    )
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
