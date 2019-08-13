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
from rest_framework.response import Response
from mrDatabaseModels.models import DeliveryRoutes, Productgroupnames
from mrDatabaseModels.schema import ProductGroupNameType, DeliveryRoutesType
from .microServiceAccountModels import AccountName, Franchise

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

class FranchiseMicroServiceType(DjangoObjectType):

    rowid = graphene.Int()
   
    class Meta:
        model = Franchise 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'franchiseName': ['exact', 'icontains', 'istartswith'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

class AccountNameMicroServiceType(DjangoObjectType):

    rowid = graphene.Int()
    productGroupid = graphene.Field(ProductGroupNameType)
    routeid = graphene.Field(DeliveryRoutesType)

    class Meta:
        model = AccountName 
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'accountMRid': ['exact', 'icontains', 'istartswith'],
            'accountName': ['exact', 'icontains', 'istartswith'],
            'commonName': ['exact', 'icontains', 'istartswith'],
            'parentAccountid': ['exact'],
            'accountDetails': ['exact'],
            'accountAccessDBid': ['exact'],
            'franchise': ['exact'],
        }

    def resolve_rowid(self, context, **kwargs):
        return self.id

    def resolve_productGroupid(self, context, **kwargs):
        return Productgroupnames.objects.get(id=self.productGroupid)

    def resolve_routeid(self, context, **kwargs):
        return DeliveryRoutes.objects.get(id=self.routeid)

class Query(graphene.ObjectType):

    node_account_name_micro_service = DjangoFilterConnectionField(AccountNameMicroServiceType)
    node_franchise_micro_service = DjangoFilterConnectionField(FranchiseMicroServiceType)

    def resolve_node_account_name_micro_service(self, context, *args, **kwargs):
        return AccountName.objects.using('accountDetailsMicroService').all()

    def resolve_node_franchise_micro_service(self, context, *args, **kwargs):
        return Franchise.objects.using('accountDetailsMicroService').all()



                