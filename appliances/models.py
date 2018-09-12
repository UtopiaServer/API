from django.db import models

# Create your models here.


class Appliance(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    country = models.TextField()
    way_of_known = models.IntegerField()
    discord_handle = models.TextField()
    minecraft_username = models.TextField()
    have_you = models.TextField()
    gamemodes = models.TextField()
    expectations = models.TextField()
    appliance = models.TextField()