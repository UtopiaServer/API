from django.db import models
from characters.models import Character

# Create your models here.

class Faction(models.Model):
    name = models.TextField()
    members = models.ManyToManyField(
        Character,
        through='Membership',
        through_fields=('faction', 'character')
    )

class Membership(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name="invitations"
    )