"""File registering models used on the app."""

from django.db import models


class Appliance(models.Model):
    """Submitted appliance model."""

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
