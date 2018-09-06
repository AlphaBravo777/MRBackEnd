import graphene

from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node

from .models import Productlist, ProcessedStockAmounts, StockTakingTimes, Productcontainers, Productcontainernames

class ProductlistType(DjangoObjectType):
    class Meta:
        model = Productlist 
        interfaces = (Node, )
        filter_fields = {
            'productid': ['exact'],
            'proddescription': ['exact', 'icontains', 'istartswith'],
        }

class ProcessedStockAmountsType(DjangoObjectType):
    class Meta:
        model = ProcessedStockAmounts 

class StockTakingTimesType(DjangoObjectType):
    class Meta:
        model = StockTakingTimes 
        interfaces = (Node, )                                   # If you add these lines, then the id will change from django-id to graphql-id
        filter_fields = {                                       # If you add these lines, then the id will change from django-id to graphql-id
            'times': ['exact', 'icontains', 'istartswith'],     # If you add these lines, then the id will change from django-id to graphql-id
        }

class ProductcontainersType(DjangoObjectType):
    class Meta:
        model = Productcontainers 

class ProductcontainernamesType(DjangoObjectType):
    class Meta:
        model = Productcontainernames 

class SearchProductlist(graphene.Union):
    class Meta:
        types = (ProductlistType,)

class Query(graphene.ObjectType):
    
    all_productlists = graphene.List(ProductlistType)
    all_processedStockAmountss = graphene.List(ProcessedStockAmountsType)
    all_stockTakingTimess = graphene.List(StockTakingTimesType)
    all_productcontainerss = graphene.List(ProductcontainersType)
    all_productcontainernamess = graphene.List(ProductcontainernamesType)
    productlist2 = Node.Field(ProductlistType) # This only works with the graphql id, and not the django id

    product = graphene.Field(ProductlistType,id=graphene.Int())
    all_products = DjangoFilterConnectionField(ProductlistType)

    all_times = DjangoFilterConnectionField(StockTakingTimesType)

    # search = graphene.Field(ProductlistType,id=graphene.Int())

    def resolve_all_productlists(self, context, **kwargs):
        return Productlist.objects.all()

    def resolve_all_processedStockAmountss(self, context, **kwargs):
        return ProcessedStockAmounts.objects.all()

    def resolve_all_stockTakingTimess(self, context, **kwargs):
        return StockTakingTimes.objects.all()

    def resolve_all_productcontainerss(self, context, **kwargs):
        return Productcontainers.objects.all()

    def resolve_all_productcontainernamess(self, context, **kwargs):
        return Productcontainernames.objects.all()
    
    def resolve_product(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Productlist.objects.get(pk=id)

        return None
