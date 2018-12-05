from django.db import models

# Create your models here.


class Character(models.Model):
    status = models.IntegerField()
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    age = models.IntegerField()

    def __unicode__(self):
        return u"{0} {1}".format(self.first_name, self.last_name)
