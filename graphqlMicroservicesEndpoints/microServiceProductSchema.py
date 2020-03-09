import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.fields import DjangoConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List, Field
from django.db.models import Q
import json
import collections
import requests
# from rest_framework.response import Response
# from mrDatabaseModels.models import DeliveryRoutes, Productgroupnames
# from mrDatabaseModels.schema import ProductGroupNameType, DeliveryRoutesType
# from .microServiceAccountModels import AccountName, Franchise
from .microServiceProductModels import MeasuringUnit, Packaging, Item, ItemBuildingBlocks, CalculatedPrice, Department, Category, Group, ItemGrouping, ItemVendor

def _json_object_hook(d):
    return collections.namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

'''
If you only have a pure json object, then you need to convert it into a python object: The only thing left to do is to convert 
our JSON dictionary to objects, so that instead of calling reviews[0]["role"] we would be able to call reviews[0].role
According to Graphene design, objects are expected to be returned by a resolver. So here is what we are going to do: serialize our JSON,
then deserialize it into objects using object_hook which would convert everything into named tuples: json2obj(json.dumps(jsonData))


json data = {'id': '18', 'routeName': 'Please show me', 'loadingDay': '4'} // Even if you use items with " ", it will change it to ' '
json.dumps data = {"id": "18", "routeName": "Please show me", "loadingDay": "4"} 
json2obj data = X(id='18', routeName='Please show me', loadingDay='4')
    
For returning a single record: (This is if you field name is "graphene.Field") data = requests.get(url)  //  data2 = json2obj(data.content)[0]  //  return data2
For returning multiple records: (Same as the above, but you field name must be a "graphene.List", and pass in the whole array, not just the first item)
'''

class MeasuringUnitType(DjangoObjectType):

    rowid = graphene.Int()
   
    class Meta:
        model = MeasuringUnit 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'unit': ['exact', 'icontains', 'istartswith'],
            'convertionToMainUnitAmount': ['exact', 'icontains', 'istartswith'],
            'mainUnit': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class ItemVendorType(DjangoObjectType):
    
    rowid = graphene.Int()
   
    class Meta:
        model = ItemVendor 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class PackagingProdType(DjangoObjectType):

    rowid = graphene.Int()

    class Meta:
        model = Packaging 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'packaging': ['exact', 'icontains', 'istartswith'],
            'weight': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class ItemType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = Item 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'size': ['exact'],
            'unit': ['exact'],
            'active': ['exact'],
            'packaging': ['exact'],
            'price': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class ItemBuildingBlocksType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = ItemBuildingBlocks 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'itemid': ['exact'],
            'buildingBlock': ['exact'],
            'quantity': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class CalculatedPriceType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = CalculatedPrice 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'itemid': ['exact'],
            'priceSource': ['exact'],
            'modifier': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class DepartmentType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = Department 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'rankingInDepartment': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class CategoryType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = Category 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'rankingInCategory': ['exact'],
            'departmentid': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class GroupType(DjangoObjectType):
    
    rowid = graphene.Int()

    class Meta:
        model = Group 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'rankingInGroup': ['exact'],
            'categoryid': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class ItemGroupingType(DjangoObjectType):

    rowid = graphene.Int()

    class Meta:
        model = ItemGrouping 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'itemid': ['exact'],
            'itemCode': ['exact', 'icontains', 'istartswith'],
            'departmentid': ['exact'],
            'catagoryid': ['exact'],
            'groupid': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class Query(graphene.ObjectType):

    node_prodms_measuring_unit = DjangoFilterConnectionField(MeasuringUnitType)
    node_prodms_item_vendor = DjangoFilterConnectionField(ItemVendorType)
    node_prodms_packaging = DjangoFilterConnectionField(PackagingProdType)
    node_prodms_item = DjangoFilterConnectionField(ItemType)
    node_prodms_item_buildingblocks = DjangoFilterConnectionField(ItemBuildingBlocksType)
    node_prodms_calculated_price = DjangoFilterConnectionField(CalculatedPriceType)
    node_prodms_department = DjangoFilterConnectionField(DepartmentType)
    node_prodms_category = DjangoFilterConnectionField(CategoryType)
    node_prodms_group = DjangoFilterConnectionField(GroupType)
    node_prodms_item_grouping = DjangoFilterConnectionField(ItemGroupingType)
    

    def resolve_node_prodms_packaging(self, context, *args, **kwargs):
        return Packaging.objects.using('productMicroService').all()

    def resolve_node_prodms_item_vendor(self, context, *args, **kwargs):
        return ItemVendor.objects.using('productMicroService').all()

    def resolve_node_prodms_measuring_unit(self, context, *args, **kwargs):
        return MeasuringUnit.objects.using('productMicroService').all()

    def resolve_node_prodms_item(self, context, *args, **kwargs):
        return Item.objects.using('productMicroService').all()

    def resolve_node_prodms_item_buildingblocks(self, context, *args, **kwargs):
        return ItemBuildingBlocks.objects.using('productMicroService').all()

    def resolve_node_prodms_calculated_price(self, context, *args, **kwargs):
        return CalculatedPrice.objects.using('productMicroService').all()

    def resolve_node_prodms_department(self, context, *args, **kwargs):
        return Department.objects.using('productMicroService').all()

    def resolve_node_prodms_category(self, context, *args, **kwargs):
        return Category.objects.using('productMicroService').all()

    def resolve_node_prodms_group(self, context, *args, **kwargs):
        return Group.objects.using('productMicroService').all()

    def resolve_node_prodms_item_grouping(self, context, *args, **kwargs):
        return ItemGrouping.objects.using('productMicroService').all()



    # get_account_micro_service = graphene.Field(AccountNameMicroServiceType, id=graphene.Int())

    # def resolve_node_account_name_micro_service(self, context, *args, **kwargs):
    #     return AccountName.objects.using('accountDetailsMicroService').all()

    # def resolve_node_franchise_micro_service(self, context, *args, **kwargs):
    #     return Franchise.objects.using('accountDetailsMicroService').all()

    # def resolve_get_account_micro_service(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return AccountName.objects.using('accountDetailsMicroService').get(pk=id)
    #     return None




                