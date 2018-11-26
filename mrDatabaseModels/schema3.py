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


# multiple filter fields? : https://stackoverflow.com/questions/43196733/filter-at-multiple-levels-with-graphql-and-graphene
# filtering parent and child fields: https://github.com/graphql-python/graphene/issues/537  // Thr problem this guy had looks exactly what I am looking for



class ProductcontainerNamesType(DjangoObjectType):
    class Meta:
        model = Productcontainernames 
        # interfaces = (Node, )
        # filter_fields = {
        #     'containername': ['exact', 'icontains', 'istartswith'],
        # }

class TimeStampType(DjangoObjectType):
    class Meta:
        model = TimeStamp

class ProcessedStockAmountsType(DjangoObjectType):
    class Meta:
        model = ProcessedStockAmounts 

class ProductcontainersType(DjangoObjectType):
    class Meta:
        model = Productcontainers 

class ProductcontainersCustom(ObjectType):
    id = ID()
    deleteContainerAmount = String()
    containernameid = String()
    productid = String()
    amount = List(ProcessedStockAmountsType, prod=graphene.String())
    time = List(TimeStampType)

    def resolve_amount(self, context, **kwargs):
        productid = kwargs.get('prod')
        print(kwargs)
        # return ProcessedStockAmounts.objects.filter(Q(timeStampID__id=2) & Q(prodName__id=productid))
        return ProcessedStockAmounts.objects.filter(prodName__productid=productid)
    # def resolve_containernameid(self, context, **kwargs):
    #     return Productcontainernames.objects.all()

        # def resolve_orders(self, args, context, info):
        # return OrdersModel.query.filter_by(customer_id=self.id).all()

class ProductlistType(DjangoObjectType):
    class Meta:
        model = Productlist 



class ProcessedStockAmountsNode(DjangoObjectType):
    class Meta:
        model = ProcessedStockAmounts 

        interfaces = (Node, )
        filter_fields = {
            'timeStampID': ['exact'],
        }

class ProcessedStockAmountsCustom(ObjectType):
    # id = ID()
    time = List(ProductlistType)
    # orders = List(Order)

    def resolve_time(self, context, **kwargs):
        return Productlist.objects.filter(id__lte=2)

    # def resolve_id(self, context, **kwargs):
    #     # return TimeStamp.objects.filter(self.id=2)
    #     key = self.id
    #     # return ProcessedStockAmounts.objects.filter(timeStampID=2)
    #     return ProcessedStockAmounts.objects.all()

    # class ProcessedStockAmountsCustom(DjangoObjectType):
    # class Meta:
    #     model = ProcessedStockAmounts 

    # def resolve_id(self, context, **kwargs):
    #     # return TimeStamp.objects.filter(self.id=2)
    #     key = self.id
    #     # return ProcessedStockAmounts.objects.filter(timeStampID=2)
    #     return ProcessedStockAmounts.objects.all()




    # def resolve_id(self, context, **kwargs):
        # return TimeStamp.objects.filter(self.id=2)
        # key = self.id
        # return ProcessedStockAmounts.objects.filter(timeStampID=2)
        # return TimeStamp.query.filter_by(pk=2).all()
        # return OrdersModel.query.filter_by(customer_id=self.id).all()

        # interfaces = (Node, )
        # filter_fields = {
        #     'year': ['exact', 'icontains', 'istartswith'],
        # }



class Query(graphene.ObjectType):

    # filter_productcontainernames_node = DjangoFilterConnectionField(ProductcontainerNamesType)
    list_productcontainernames = graphene.List(ProductcontainerNamesType)
    list_productcontainers = graphene.List(ProductcontainersType)
    list_productlists = graphene.List(ProductlistType)
    list_processedstockamounts = graphene.List(ProcessedStockAmountsType)

    list_processedstockamountscustom = graphene.List(ProcessedStockAmountsCustom)
    list_productcontainerscustom = graphene.List(ProductcontainersCustom)
    # list_timestamp = graphene.List(TimeStampType)

    filter_processedstockamounts_node = DjangoFilterConnectionField(ProcessedStockAmountsNode)

    filter_productcontainernames = graphene.Field(ProductcontainerNamesType, containername=graphene.String(), id=graphene.Int())
    filter_timestamp = graphene.Field(TimeStampType, id=graphene.Int())
    filter_processedstockamounts = graphene.List(ProcessedStockAmountsType, id=graphene.Int(), timeStampID=graphene.Int())
    custom_filter_productcontainers = graphene.List(ProductcontainersType, id=graphene.Int(), timeStampID=graphene.Int())

    def resolve_custom_filter_productcontainers(self, context, **kwargs):
        timeStampID = kwargs.get('timeStampID')
        if timeStampID is not None:
            return Productcontainers.objects.filter()
        return None

    def resolve_filter_productcontainernames(self, context, **kwargs):
        id = kwargs.get('id')
        containername = kwargs.get('containername')
        if containername is not None:
            return Productcontainernames.objects.get(containername=containername)
        elif id is not None:
            return Productcontainernames.objects.get(pk=id)
        return None

    def resolve_filter_timestamp(self, context, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return TimeStamp.objects.get(pk=id)
        return None

    def resolve_filter_processedstockamounts(self, context, **kwargs):
        timeStampID = kwargs.get('timeStampID')
        if timeStampID is not None:
            return ProcessedStockAmounts.objects.filter(timeStampID=timeStampID)
        return None

    def resolve_list_productcontainernames(self, context, **kwargs):
        return Productcontainernames.objects.all()

    def resolve_list_productcontainers(self, context, **kwargs):
        return Productcontainers.objects.all()
        # The line worked to return just one item that is three models deep
        # return Productcontainers.objects.filter(productid__packaging__packaging_type='Box')
        # return Productcontainers.objects.filter(productid__processedstockamounts__timeStampID__id=3) 
        # return Productcontainers.objects.exclude(productid__processedstockamounts__timeStampID__id__lte=2)
        # e = Entry.objects.select_related('blog').get(id=5)


    def resolve_list_productlists(self, context, **kwargs):
        return Productlist.objects.all()

    def resolve_list_processedstockamounts(self, context, **kwargs):
        return ProcessedStockAmounts.objects.all()

    def resolve_list_timestamp(self, context, **kwargs):
        return TimeStamp.objects.all()

    def resolve_list_processedstockamountscustom(self, context, **kwargs):
        return ProcessedStockAmounts.objects.all()

    def resolve_list_productcontainerscustom(self, context, **kwargs):
        return Productcontainers.objects.all()

# class ProductlistType(DjangoObjectType):
#     class Meta:
#         model = Productlist 
#         interfaces = (Node, )
#         filter_fields = {
#             'productid': ['exact'],
#             'proddescription': ['exact', 'icontains', 'istartswith'],
#             'productonhold': ['exact'],
#         }

# class ProcessedStockAmountsType(DjangoObjectType):
#     class Meta:
#         model = ProcessedStockAmounts 
#         interfaces = (Node, )
#         filter_fields = {
#             'amount': ['exact'],
#             'timeStampID': ['exact'],
            
#         }

# class TimeStampType(DjangoObjectType):
#     class Meta:
#         model = TimeStamp 
#         interfaces = (Node, )
#         filter_fields = {
#             'year': ['exact'],
#             'id': ['exact'],
#         }

# class StockTakingTimesType(DjangoObjectType):
#     class Meta:
#         model = StockTakingTimes 
#         interfaces = (Node, )                                   # If you add these lines, then the id will change from django-id to graphql-id
#         filter_fields = {                                       # If you add these lines, then the id will change from django-id to graphql-id
#             'times': ['exact', 'icontains', 'istartswith'],     # If you add these lines, then the id will change from django-id to graphql-id
#         }

# class ProductcontainersType(DjangoObjectType):
#     class Meta:
#         model = Productcontainers 

# class ProductcontainernamesType(DjangoObjectType):
#     class Meta:
#         model = Productcontainernames 

# class SearchProductlist(graphene.Union):
#     class Meta:
#         types = (ProductlistType,)

# class ProductBrandsType(DjangoObjectType):
#     class Meta:
#         model = ProductBrands 

# class PackagingType(DjangoObjectType):
#     class Meta:
#         model = Packaging 

# class ColorCodesType(DjangoObjectType):
#     class Meta:
#         model = ColorCodes 
        
# class MeasuringUnitsType(DjangoObjectType):
#     class Meta:
#         model = MeasuringUnits 

# class HighRiskPackingListType(DjangoObjectType):
#     class Meta:
#         model = HighRiskPackingList 
#         interfaces = (Node, )
#         filter_fields = {
#             'currentStock': ['exact', 'icontains', 'istartswith'],
#         }

# class BatchgroupsType(DjangoObjectType):
#     class Meta:
#         model = Batchgroups

# #--------------------------------------------------------------------------------------


# class Query(graphene.ObjectType):
    
#     # This just gives a normal list of products without any filtering (Model must be in here to show up in other models)
#     all_productlists = graphene.List(ProductlistType)
#     all_timeStamps = graphene.List(TimeStampType)
#     all_processedStockAmountss = graphene.List(ProcessedStockAmountsType)
#     all_stockTakingTimess = graphene.List(StockTakingTimesType)
#     all_productcontainerss = graphene.List(ProductcontainersType)
#     all_productcontainernamess = graphene.List(ProductcontainernamesType)
#     all_highRiskPackingList = graphene.List(HighRiskPackingListType)
#     all_batchgroups = graphene.List(BatchgroupsType)
#     all_productBrands = graphene.List(ProductBrandsType)
#     all_packaging = graphene.List(PackagingType)
#     all_colorCodes = graphene.List(ColorCodesType)
#     all_measuringUnits = graphene.List(MeasuringUnitsType)

#     # * This goes with the other star marked as resolved
#     testTimeStamp = graphene.Field(TimeStampType, id=graphene.Int())
    
#     productlist2 = Node.Field(ProductlistType) # This only works with the graphql id, and not the django id (Doesn't work well)

#     # This is if you want to get a field with the DB standard id value (in Int format) NB!! Use the resolve fields right at the bottom as well!!
#     product = graphene.Field(ProductlistType, id=graphene.Int())
#     processedStock = graphene.Field(ProcessedStockAmountsType, id=graphene.Int())
#     time_stamp_filter = graphene.Field(TimeStampType, id=graphene.Int())
    
#     # This is where you add a Type if you want to filter it (Set the fields that can be filtered in the type itself)
#     filter_processedStockAmounts = DjangoFilterConnectionField(ProcessedStockAmountsType, pk=graphene.Int())
#     filter_timeStamp = DjangoFilterConnectionField(TimeStampType)
#     all_products = DjangoFilterConnectionField(ProductlistType)
#     all_times = DjangoFilterConnectionField(StockTakingTimesType)
#     filter_highRiskPackingList = DjangoFilterConnectionField(HighRiskPackingListType)

#     # search = graphene.Field(ProductlistType,id=graphene.Int())

#     # def resolve_testTimeStamp(self, args, context, info):
#     #     query = TimeStampType.get_query(context)
#     #     return query.get(args.get('pk'))

#     def resolve_all_productlists(self, context, **kwargs):
#         return Productlist.objects.all()

#     def resolve_all_timeStamps(self, context, **kwargs):
#         return TimeStamp.objects.all()

#     def resolve_all_processedStockAmountss(self, context, **kwargs):
#         return ProcessedStockAmounts.objects.all()

#     def resolve_all_stockTakingTimess(self, context, **kwargs):
#         return StockTakingTimes.objects.all()

#     def resolve_all_productcontainerss(self, context, **kwargs):
#         return Productcontainers.objects.all()

#     def resolve_all_productcontainernamess(self, context, **kwargs):
#         return Productcontainernames.objects.all()

#     def resolve_all_highRiskPackingList(self, context, **kwargs):
#         return HighRiskPackingList.objects.all()

#     def resolve_all_batchgroups(self, context, **kwargs):
#         return Batchgroups.objects.all()
    
#     def resolve_all_productBrands(self, context, **kwargs):
#         return ProductBrands.objects.all()

#     def resolve_all_packaging(self, context, **kwargs):
#         return Packaging.objects.all()

#     def resolve_all_colorCodes(self, context, **kwargs):
#         return ColorCodes.objects.all()

#     def resolve_all_measuringUnits(self, context, **kwargs):
#         return MeasuringUnits.objects.all()

#     def resolve_product(self, context, **kwargs):
#         id = kwargs.get('id')
#         if id is not None:
#             return Productlist.objects.get(pk=id)
#         return None

#     def resolve_time_stamp_filter(self, context, **kwargs):
#         id = kwargs.get('id')
#         if id is not None:
#             return TimeStamp.objects.get(pk=id)
#         return None





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