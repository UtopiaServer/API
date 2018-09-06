import graphene
from graphene_django import DjangoObjectType
from launcher.models import Mod, Revision, Namespace


class ModType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Mod

class RevisionType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Revision

class NamespaceType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Namespace
