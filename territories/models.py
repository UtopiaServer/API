from django.db import models
from factions.models import Faction

# Create your models here.

class Territory(models.Model):
    name = models.TextField()
    minX = models.IntegerField()
    minY = models.IntegerField()
    minZ = models.IntegerField()
    maxX = models.IntegerField()
    maxY = models.IntegerField()
    maxZ = models.IntegerField()
    dimension = models.IntegerField()
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)