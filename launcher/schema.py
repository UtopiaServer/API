import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from launcher.models import Mod, Revision, Namespace
from launcher.types import ModType, RevisionType, NamespaceType
import itertools


class CreateNamespace(graphene.Mutation):
    
    id = graphene.Int()
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        namespace = Namespace.objects.create(
            name=name
        )

        return CreateNamespace(
            id=namespace.id,
            name=namespace.name
        )


class DeleteNamespace(graphene.Mutation):

    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        namespace = Namespace.objects.filter(id=id).first()

        if namespace is None:
            raise Exception("Could not find the associated namespace.")

        namespace.delete()

        return DeleteNamespace(
            id=id
        )


class AddModToNamespace(graphene.Mutation):

    id = graphene.Int()
    version = graphene.String()
    md5 = graphene.String()
    url = graphene.String()
    namespace = graphene.Field(NamespaceType)

    class Arguments:
        namespace_id = graphene.Int()
        version = graphene.String()
        md5 = graphene.String()
        url = graphene.String()

    def mutate(self, info, version, md5, url, namespace_id):
        namespace = Namespace.objects.filter(id=namespace_id).first()

        if namespace is None:
            raise Exception("No namespace found for this ID")

        mod = Mod.objects.create(
            version=version,
            md5=md5,
            url=url,
            namespace=namespace
        )

        return AddModToNamespace(
            id=mod.id,
            version=version,
            md5=md5,
            url=url,
            namespace=namespace
        )


class RemoveModFromNamespace(graphene.Mutation):

    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        mod = Mod.objects.filter(id=id).first()

        if mod is None:
            raise Exception("Could not find the associated mod.")

        mod.delete()

        return RemoveModFromNamespace(
            id=id
        )




class CreateRevision(graphene.Mutation):
    
    id = graphene.Int()
    version = graphene.String()

    class Arguments:
        version = graphene.String()

    def mutate(self, info, version):
        revision = Revision.objects.create(
            version=version
        )

        return CreateRevision(
            id=revision.id,
            version=revision.version
        )


class DeleteRevision(graphene.Mutation):

    id = graphene.Int()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        revision = Revision.objects.filter(id=id).first()

        if revision is None:
            raise Exception("Could not find the associated revision.")

        revision.delete()

        return DeleteRevision(
            id=id
        )


class AddModToRevision(graphene.Mutation):

    mod = graphene.Field(ModType)
    revision = graphene.Field(RevisionType)

    class Arguments:
        revision_id = graphene.Int()
        mod_id = graphene.Int()

    def mutate(self, info, revision_id, mod_id):
        revision = Revision.objects.filter(id=revision_id).first()

        if revision is None:
            raise Exception("Could not find the associated revision.")

        mod = Mod.objects.filter(id=mod_id).first()

        if mod is None:
            raise Exception("Could not find the associated mod.")

        revision_mod = RevisionMod.objects.create(
            revision=revision,
            mod=mod
        )

        return AddModToRevision(
            revision=revision,
            mod=mod
        )


class RemoveModFromRevision(graphene.Mutation):

    mod = graphene.Field(ModType)
    revision = graphene.Field(RevisionType)

    class Arguments:
        revision_id = graphene.Int()
        mod_id = graphene.Int()

    def mutate(self, info, revision_id, mod_id):
        revision = Revision.objects.filter(id=revision_id).first()

        if revision is None:
            raise Exception("Could not find the associated revision.")

        mod = Mod.objects.filter(id=mod_id).first()

        if mod is None:
            raise Exception("Could not find the associated mod.")

        revision_mod = RevisionMod.objects.filter(
            revision=revision,
            mod=mod
        ).first()

        if revision_mod is None:
            raise Exception("No link found")

        return RemoveModFromRevision(
            revision=revision,
            mod=mod
        )



class Query(graphene.ObjectType):
    namespaces = graphene.List(NamespaceType, id=graphene.Int(), name=graphene.String())
    revisions = graphene.List(RevisionType, id=graphene.Int(), version=graphene.String())

    def resolve_namespaces(self, info, id=None, name=None, **kwargs):
        namespaces = Namespace.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            namespaces = namespaces.filter(filter)
        if name is not None and id is None:
            filter = (
                Q(name__startswith=name)
            )
            namespaces = namespaces.filter(filter)
        return namespaces
    
    def resolve_revisions(self, info, id=None, version=None, **kwargs):
        revisions = Revision.objects.all()
        if id:
            filter = (
                Q(id=id)
            )
            revisions = revisions.filter(filter)
        if version is not None and id is None:
            filter = (
                Q(version__startswith=version)
            )
            revisions = revisions.filter(filter)
        return revisions


class Mutation(graphene.ObjectType):
    create_revision = CreateRevision.Field()
    delete_revision = DeleteRevision.Field()
    create_namespace = CreateNamespace.Field()
    delete_namespace = DeleteNamespace.Field()
    add_mod_to_revision = AddModToRevision.Field()
    add_mod_to_namespace = AddModToNamespace.Field()
    remove_mod_from_revision = RemoveModFromRevision.Field()
    remove_mod_from_namespace = RemoveModFromNamespace.Field()

