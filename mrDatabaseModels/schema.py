import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import relay
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
                    MeasuringUnits, \
                    Factoryarea, \
                    Factorysubarea, \
                    Image


# multiple filter fields? : https://stackoverflow.com/questions/43196733/filter-at-multiple-levels-with-graphql-and-graphene
# filtering parent and child fields: https://github.com/graphql-python/graphene/issues/537  // Thr problem this guy had looks exactly what I am looking for

class ProductlistType(DjangoObjectType):
    class Meta:
        model = Productlist 
        interfaces = (relay.Node, )
        filter_fields = {
            'productid': ['exact'],
            'proddescription': ['exact', 'icontains', 'istartswith'],
            'productonhold': ['exact'],
            'packaging': ['exact'],
        }

class ProcessedStockAmountsType(DjangoObjectType):
    class Meta:
        model = ProcessedStockAmounts 
        interfaces = (Node, )
        filter_fields = {
            'amount': ['exact'],
            'timeStampID': ['exact'],
        }

class TimeStampType(DjangoObjectType):
    rowid=graphene.Int()
    class Meta:
        model = TimeStamp 
        interfaces = (Node, )
        filter_fields = {
            'id': ['exact'],
            'year': ['exact'],
            'week': ['exact'],
            'weekDay': ['exact'],
            'shift': ['exact'],
            'time': ['exact'],
            'shortDate': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class StockTakingTimesType(DjangoObjectType):
    class Meta:
        model = StockTakingTimes 
        interfaces = (Node, )                                   # If you add these lines, then the id will change from django-id to graphql-id
        filter_fields = {                                       
            'times': ['exact', 'icontains', 'istartswith'],     
        }

class ProductcontainersType(DjangoObjectType):
    rowid=graphene.Int()
    class Meta:
        model = Productcontainers 
        interfaces = (Node, )  
        filter_fields = {       
            'productid': ['exact',],                                 
            'deleteContainerAmount': ['exact', 'icontains', 'istartswith'],     
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id
        

class ProductcontainernamesType(DjangoObjectType):
    class Meta:
        model = Productcontainernames 
        interfaces = (Node, )
        filter_fields = {                                       
            'containername': ['exact', 'icontains', 'istartswith'],     
        }  

class ProductBrandsType(DjangoObjectType):
    class Meta:
        model = ProductBrands 
        interfaces = (Node, )
        filter_fields = {                                       
            'brand': ['exact', 'icontains', 'istartswith'],     
        }  

class PackagingType(DjangoObjectType):
    class Meta:
        model = Packaging 
        interfaces = (Node, )
        filter_fields = {                                       
            'packaging_type': ['exact', 'icontains', 'istartswith'],     
        }  

class ColorCodesType(DjangoObjectType):
    class Meta:
        model = ColorCodes 
        interfaces = (Node, )
        filter_fields = {                                       
            'colorCode': ['exact', 'icontains', 'istartswith'],     
        }  
        
class MeasuringUnitsType(DjangoObjectType):
    class Meta:
        model = MeasuringUnits 
        interfaces = (Node, )
        filter_fields = {                                       
            'unitAmount': ['exact', 'icontains', 'istartswith'],   
            'measuringUnit': ['exact', 'icontains', 'istartswith'],    
        }  

class HighRiskPackingListType(DjangoObjectType):
    class Meta:
        model = HighRiskPackingList 
        interfaces = (Node, )
        filter_fields = {
            'currentStock': ['exact', 'icontains', 'istartswith'],
            'stockNeeded': ['exact', 'icontains', 'istartswith'],
        }

class BatchgroupsType(DjangoObjectType):
    class Meta:
        model = Batchgroups
        interfaces = (Node, )
        filter_fields = {
            'batchname': ['exact', 'icontains', 'istartswith'],
            'ranking': ['exact', 'icontains', 'istartswith'],
        }

class FactoryAreaType(DjangoObjectType):
    class Meta:
        model = Factoryarea
        interfaces = (Node, )
        filter_fields = {
            'area': ['exact', 'icontains', 'istartswith'],
            'areaRanking': ['exact', 'icontains', 'istartswith'],
        }

class FactorySubAreaType(DjangoObjectType):
    class Meta:
        model = Factorysubarea
        interfaces = (Node, )
        filter_fields = {
            'area': ['exact',],
            'subArea': ['exact', 'icontains', 'istartswith'],
            'subAreaRanking': ['exact', 'icontains', 'istartswith'],
        }

class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        interfaces = (Node, )
        filter_fields = {
            'imageName': ['exact', 'icontains', 'istartswith'],
        }

#--------------------------------------------------------------------------------------


class Query(graphene.ObjectType):
    
    # This just gives a normal list of products without any filtering (Model must be in here to show up in other models)
    list_productlists = graphene.List(ProductlistType)
    list_timestamps = graphene.List(TimeStampType)
    list_processedstockamounts = graphene.List(ProcessedStockAmountsType)
    list_stocktakingtimes = graphene.List(StockTakingTimesType)
    list_productcontainers = graphene.List(ProductcontainersType)
    list_productcontainernames = graphene.List(ProductcontainernamesType)
    list_highriskpackinglist = graphene.List(HighRiskPackingListType)
    list_batchgroups = graphene.List(BatchgroupsType)
    list_productbrands = graphene.List(ProductBrandsType)
    list_packaging = graphene.List(PackagingType)
    list_colorcodes = graphene.List(ColorCodesType)
    list_measuringunits = graphene.List(MeasuringUnitsType)
    list_images = graphene.List(ImageType)

    node_productlist = DjangoFilterConnectionField(ProductlistType)
    node_processedstockamounts = DjangoFilterConnectionField(ProcessedStockAmountsType)
    node_timestamp = DjangoFilterConnectionField(TimeStampType)
    node_stocktakingtimes = DjangoFilterConnectionField(StockTakingTimesType)
    node_productcontainers = DjangoFilterConnectionField(ProductcontainersType)
    node_productcontainernames = DjangoFilterConnectionField(ProductcontainernamesType)
    node_productbrands = DjangoFilterConnectionField(ProductBrandsType)
    node_packaging = DjangoFilterConnectionField(PackagingType)
    node_colorcodes = DjangoFilterConnectionField(ColorCodesType)
    node_measuringunits = DjangoFilterConnectionField(MeasuringUnitsType)
    node_highriskpackinglist = DjangoFilterConnectionField(HighRiskPackingListType)
    node_batchgroups = DjangoFilterConnectionField(BatchgroupsType)
    node_images = DjangoFilterConnectionField(ImageType)

    def resolve_list_productlists(self, context, **kwargs):
        return Productlist.objects.all()

    def resolve_list_timestamps(self, context, **kwargs):
        return TimeStamp.objects.all()

    def resolve_list_processedstockamounts(self, context, **kwargs):
        return ProcessedStockAmounts.objects.all()

    def resolve_list_stocktakingtimes(self, context, **kwargs):
        return StockTakingTimes.objects.all()

    def resolve_list_productcontainers(self, context, **kwargs):
        return Productcontainers.objects.all()

    def resolve_list_productcontainernames(self, context, **kwargs):
        return Productcontainernames.objects.all()

    def resolve_list_highriskpackinglist(self, context, **kwargs):
        return HighRiskPackingList.objects.all()

    def resolve_list_batchgroups(self, context, **kwargs):
        return Batchgroups.objects.all()
    
    def resolve_list_productbrands(self, context, **kwargs):
        return ProductBrands.objects.all()

    def resolve_list_packaging(self, context, **kwargs):
        return Packaging.objects.all()

    def resolve_list_colorcodes(self, context, **kwargs):
        return ColorCodes.objects.all()

    def resolve_list_measuringunits(self, context, **kwargs):
        return MeasuringUnits.objects.all()

    def resolve_list_images(self, context, **kwargs):
        return Image.objects.all()

    # def resolve_product(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return Productlist.objects.get(pk=id)
    #     return None

    # def resolve_time_stamp_filter(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return TimeStamp.objects.get(pk=id)
    #     return None


#  ---------------------  Lesson 1  --------------------------

# The below code simply gives you access to a list of all the things that is in this table. 
# There are three things in this table, but you can only query the two things that do not have a foreign key - id and containername
# The id that returns is the actual DB id and not graphql id
# You can not filter anything, you just get a full list of what ever you are add to retreave
# Changing the names of the objects (like all_productcontainernamess to list_productcontainernames) does not change anything
# This is the only way that you can get a list of records, the filter ways below will return "Null" if you do not pass in an argument
# If you use this list with the node lesson below, your id's will change to graphql id's as stated above
# The best may be to use this method for lists, along with lesson 5 for filtering
# If you really want to use first, last, i_contains, then you can maybe just create another class to use it on

# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 


# class Query(graphene.ObjectType):

#     all_productcontainernamess = graphene.List(ProductcontainernamesType)

#     def resolve_all_productcontainernamess(self, context, **kwargs):
#         return Productcontainernames.objects.all()


#  ---------------------  Lesson 2  --------------------------

# Changing the above code to the code below will give you all the filtering in the filter fields
# It will also change the id to the graphql id (meaning filtering by id becomes almost useless)
# edge and node is now used  (This looks like something that belongs to DjangoFilterConnectionField, you can filter but not by id)

# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 
#         interfaces = (Node, )
#         filter_fields = {
#             'id': ['exact'],
#             'containername': ['exact', 'icontains', 'istartswith'],
#         }


# class Query(graphene.ObjectType):

#     filter_productcontainernames = DjangoFilterConnectionField(ProductcontainernamesType)

#  ---------------------  Lesson 3  --------------------------

# Changing the above code to the code below, now allows you to filter by the DB id again, but you can ONLY filter the id, not any of the other fields
# You can basically use a given id to return all the fields for that id, but you can not filter any of the other fields
# So far I only know that you can not filter any of the other non-foreign key fields, maybe you can filter foreign key fields if you set them
# up correctly
# This is basically the exact same as lesson 1, but now you can filter on the id

# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 

# class Query(graphene.ObjectType):

#     filter_productcontainernames = graphene.Field(ProductcontainernamesType, id=graphene.Int())

#     def resolve_filter_productcontainernames(self, context, **kwargs):
#         id = kwargs.get('id')
#         if id is not None:
#             return Productcontainernames.objects.get(pk=id)
#         return None

#  ---------------------  Lesson 4  --------------------------
# The following code does exactly as lesson 3, but now you are filtering not on the id, but on the containername

# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 

# class Query(graphene.ObjectType):

#     filter_productcontainernames = graphene.Field(ProductcontainernamesType, containername=graphene.String())

#     def resolve_filter_productcontainernames(self, context, **kwargs):
#         containername = kwargs.get('containername')
#         if containername is not None:
#             return Productcontainernames.objects.get(containername=containername)
#         return None


#  ---------------------  Lesson 5  --------------------------
# The following code lets you filter by id or containernamename, so it is basically lesson 3 and 4 combined
# This now does everything so far that lesson two does, without the edge->node steps and using the DB id


# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 

# class Query(graphene.ObjectType):

#     filter_productcontainernames = graphene.Field(ProductcontainernamesType, containername=graphene.String(), id=graphene.Int())

#     def resolve_filter_productcontainernames(self, context, **kwargs):
#         id = kwargs.get('id')
#         containername = kwargs.get('containername')
#         if containername is not None:
#             return Productcontainernames.objects.get(containername=containername)
#         elif id is not None:
#             return Productcontainernames.objects.get(pk=id)
#         return None

#  ---------------------  Lesson 6  --------------------------
# Now all you need to use the data of a foreign field, is to add the field class like the code below
# You do not need a resolver or anything else, and you will once again be able to see only the fields that are not foreign-keys
# You can only use this data in a query that you have started with resolver, you can not start a query with this data.
# You can also of coarse not filter or do anything else with this data
# So with the code below, other classes can use this class, but this class can not use/list itself or other data

# class ProductcontainersType(DjangoObjectType):
#     class Meta:
#         model = Productcontainers 


# query{
#   listProductcontainers{
#   	id
#     productid{
#       productid
#       processedstockamountsSet{
# 				amount
#         timeStampID{
#           id
#         }
#       }
#     }
#     containernameid{
#       containername
#     }
#   }
# } 