import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.fields import DjangoConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List, Field, Float
from django.db.models import Q, F, Sum, FloatField
import json
import collections
import requests
from rest_framework.response import Response
from mrDatabaseModels.models import DeliveryRoutes, Productgroupnames, TimeStamp, Productlist
from mrDatabaseModels.schema import ProductGroupNameType, DeliveryRoutesType, TimeStampType, ProductlistType
from .microServiceOrderModels import OrderDetailsMicroService, OrderProductAmountsMicroService, TestForSETS

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

class OrderDetailsMicroServiceType(DjangoObjectType):
    # routeid = graphene.List(DeliveryRoutesType)
    rowid = graphene.Int()
    orderTotalAmount = graphene.Float()
    routeNode = graphene.Field(DeliveryRoutesType)

    class Meta:
        model = OrderDetailsMicroService 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'accountid': ['exact', 'icontains', 'istartswith'],
            'accountMRid': ['exact', 'icontains', 'istartswith'],
            'commonName': ['exact', 'icontains', 'istartswith'],
            'orderDate': ['exact', 'icontains', 'istartswith'],
            'dateCreated': ['exact', 'icontains', 'istartswith'],
            'lastModified': ['exact', 'icontains', 'istartswith'],
            'timeStampid': ['exact'],
            'routeid': ['exact'],
            'userid': ['exact'],
            'delivered': ['exact'],
            'orderNumber': ['exact'],
        }

    # def resolve_timeStampid(self, context, **kwargs):
    #     return TimeStamp.objects.get(id=self.timeStampid)

    def resolve_routeNode(self, context, **kwargs):
        return DeliveryRoutes.objects.get(id=self.routeid)

    def resolve_rowid(self, context, **kwargs):
        return self.id

    def resolve_orderTotalAmount(self, context, **kwargs):
        total = OrderProductAmountsMicroService.objects.using('orderDetailsMicroService') \
        .filter(orderDetailsid=self.id) \
        .aggregate(totalSum=Sum(F('amount')*F('packageWeight'), output_field=FloatField()))
        print('The total for the route = ', total['totalSum'])
        return total['totalSum']

class OrderProductAmountsMicroServiceType(DjangoObjectType):
    
    rowid = graphene.Int()
    productid = graphene.Field(ProductlistType)


    class Meta:
        model = OrderProductAmountsMicroService 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'orderDetailsid': ['exact'],
            # 'productid': ['exact'],
            'productMRid': ['exact', 'icontains', 'istartswith'],
            'amount': ['exact'],
            'status': ['exact'],
            'lastModified': ['exact', 'icontains', 'istartswith'],
            'userid': ['exact'],
            'packageWeight': ['exact', 'icontains', 'istartswith'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

    def resolve_productid(self, context, **kwargs):
        return Productlist.objects.get(id=self.productid)

class TestForSETSMicroServiceType(DjangoObjectType):
        
    rowid = graphene.Int()

    class Meta:
        model = TestForSETS 
        interfaces = (relay.Node, )
        filter_fields = {
            'productid': ['exact', 'icontains', 'istartswith'],
            'orderDetailsid': ['exact'],
            'product': ['exact'],
            'route': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class Query(graphene.ObjectType):

    # list_micro_account_names_search = graphene.List(MicroAccountNameType, id=Int(), accountMRid=String(), commonName=String())

    node_order_details_micro_service = DjangoFilterConnectionField(OrderDetailsMicroServiceType)
    node_order_products_amounts_micro_service = DjangoFilterConnectionField(OrderProductAmountsMicroServiceType)
    # node_test_for_sets_micro_service = DjangoFilterConnectionField(TestForSETSMicroServiceType)

    def resolve_node_order_details_micro_service(self, context, *args, **kwargs):
        return OrderDetailsMicroService.objects.using('orderDetailsMicroService').all()

    def resolve_node_order_products_amounts_micro_service(self, context, *args, **kwargs):
        return OrderDetailsMicroService.objects.using('OrderProductAmountsMicroService').all()





                