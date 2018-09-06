from django.db import models

# Create your models here.


class Namespace(models.Model):

    name = models.TextField()


class Mod(models.Model):

    version = models.CharField(max_length=32)
    url = models.URLField()
    md5 = models.CharField(max_length=32)

    namespace = models.ForeignKey(
        Namespace,
        on_delete=models.CASCADE,
        related_name="files"
    )

class Revision(models.Model):

    version = models.CharField(max_length=32)
    mods = models.ManyToManyField(
        Mod,
        through='RevisionMod',
        through_fields=('revision', 'mod')
    )


class RevisionMod(models.Model):
    revision = models.ForeignKey(Revision, on_delete=models.CASCADE)
    mod = models.ForeignKey(Mod, on_delete=models.CASCADE)