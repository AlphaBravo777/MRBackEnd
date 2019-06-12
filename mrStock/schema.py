import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List
from django.db.models import Q

from .models import HPPMeatriteStock, \
                    HPPProductStatus

class HPPMeatriteStockType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = HPPMeatriteStock 
        interfaces = (relay.Node, )
        filter_fields = {
            'productid': ['exact'],
            'batchNumberJunctionid': ['exact'],
            'amount': ['exact', 'icontains', 'istartswith'],
            'productStatusid': ['exact'],
            'userid': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id


class HPPProductStatusType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = HPPProductStatus 
        interfaces = (relay.Node, )
        filter_fields = {
            'productStatus': ['exact', 'icontains', 'istartswith'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class Query(graphene.ObjectType):

    node_hppMeatriteStock = DjangoFilterConnectionField(HPPMeatriteStockType)
    node_hppProductStatus = DjangoFilterConnectionField(HPPProductStatusType)