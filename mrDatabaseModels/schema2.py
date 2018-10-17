import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import ID, String, Int, List
from django.db.models import Q

from .models import Productlist, \
                    ProcessedStockAmounts, \
                    StockTakingTimes, \
                    Productcontainers, \
                    Productcontainernames, \
                    HighRiskPackingList, \
                    Batchgroups, \
                    TimeStamp, \
                    ProductBrands, \
                    Packaging, \
                    ColorCodes, \
                    MeasuringUnits

class ProductcontainerNamesType(DjangoObjectType):
    class Meta:
        model = Productcontainernames 

class TimeStampType(DjangoObjectType):
    rowid=graphene.Int()
    class Meta:

        model = TimeStamp
        interfaces = (Node, )
        filter_fields = {
            'year': ['exact'],
            'week': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

# class ProcessedStockAmountsType(DjangoObjectType):
#     class Meta:
#         model = ProcessedStockAmounts 

# class ProcessedStockAmountsType(DjangoObjectType):
#     # timeStampID = graphene.Field(TimeStampType, id=graphene.Int())
#     class Meta:
#         model = ProcessedStockAmounts 

#     # def resolve_timeStampID(self, info, **kwargs):
#     #     id = kwargs.get('id')
#     #     if self.timeStampID.id == id:
#     #         return self.timeStampID

class ProcessedStockAmountsNode(DjangoObjectType):
    class Meta:
        model = ProcessedStockAmounts 
        interfaces = (Node, )
        filter_fields = {
            'timeStampID': ['exact'],
            'amount': ['exact'],
        }

class ProductcontainersType(DjangoObjectType):
    class Meta:
        model = Productcontainers 

class ProductlistType(DjangoObjectType):
    class Meta:
        model = Productlist 

class Query(graphene.ObjectType):

    # list_productcontainernames = graphene.List(ProductcontainerNamesType)
    list_productcontainers = graphene.List(ProductcontainersType)
    # list_productlists = graphene.List(ProductlistType)
    # list_processedstockamounts = graphene.List(ProcessedStockAmountsType)


    # filter_timestampid = graphene.List(TimeStampType, id=graphene.Int())
    # filter_productcontainernames = graphene.Field(ProductcontainerNamesType, containername=graphene.String(), id=graphene.Int())
    # filter_productlists = graphene.Field(ProductlistType, id=graphene.Int())
    # filter_processedstockamounts = graphene.Field(ProcessedStockAmountsNode, timestampid=graphene.Int())

    filter_processedstockamounts_node = DjangoFilterConnectionField(ProcessedStockAmountsNode)
    filter_timestanpid_node = DjangoFilterConnectionField(TimeStampType)

    def resolve_list_productlists(self, context, **kwargs):
        return Productlist.objects.all()

    def resolve_list_productcontainernames(self, context, **kwargs):
        return Productcontainernames.objects.all()

    def resolve_list_productcontainers(self, context, **kwargs):
        return Productcontainers.objects.all()

    # def resolve_filter_productcontainernames(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     containername = kwargs.get('containername')
    #     if containername is not None:
    #         return Productcontainernames.objects.get(containername=containername)
    #     elif id is not None:
    #         return Productcontainernames.objects.get(pk=id)
    #     return None

    # def resolve_filter_timestampid(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return TimeStamp.objects.get(pk=id)
    #     return None

    # def resolve_filter_processedstockamounts(self, context, **kwargs):
    #     timestamp = kwargs.get('timestampid')
    #     if timestamp is not None:
    #         return ProcessedStockAmounts.objects.get(timeStampID=timestamp)
    #     return None

#  Getting the data with the global id
# query{
#   listProductcontainers{
#     id
#     containernameid{
#       containername
#     }
#     productid{
#       processedstockamountsSet(timeStampID:"VGltZVN0YW1wVHlwZToy"){
#         edges{
#           node{
#             amount
#             timeStampID{
#               id
#               rowid
#             }
#           }
#         }
#       }
#     }
#   }
# }

#Getting the global id
# query{
#   filterTimestanpidNode(year:2018, week:41){
#     edges{
#       node{
#         id
#         rowid
#       }
#     }
#   }
# }