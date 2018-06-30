from django.db import models

# Create your models here.


class World(models.Model):

    name = models.TextField()
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    state = models.BooleanField()
