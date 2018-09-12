import graphene
from graphene_django import DjangoObjectType
from appliances.models import Appliance


class ApplianceType(DjangoObjectType):

    id = graphene.Int(source='pk')

    class Meta:
        model = Appliance

