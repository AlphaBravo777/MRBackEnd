import graphene
# from django.db import models
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
from mrDatabaseModels.schema import ProductGroupNameType
from api_urls import ACCOUNT_SERVICE_URL, \
    SEARCH_ACCOUNT_COMMONNAMES, \
    GET_SINGLE_ACCOUNT_ID, \
    GET_SINGLE_ACCOUNT_MRID
# from mrDatabaseModels.schema import DeliveryRoutesType

from .models import MessageLevels, DailyReport, ChecklistAreas, Checklist, AccountName, ReportImages

def _json_object_hook(d):
    return collections.namedtuple('X', d.keys())(*d.values())

def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

class ChecklistAreaType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = ChecklistAreas 
        interfaces = (relay.Node, )
        filter_fields = {
            'area': ['exact', 'icontains', 'istartswith'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class MessageLevelsType(DjangoObjectType):
    class Meta:
        model = MessageLevels 
        interfaces = (relay.Node, )
        filter_fields = {
            'levelName': ['exact', 'icontains', 'istartswith'],
            'report': ['exact', 'icontains', 'istartswith'],
            'checklist': ['exact', 'icontains', 'istartswith'],
        }

class DailyReportType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = DailyReport 
        interfaces = (relay.Node, )
        filter_fields = {
            'timeStampID': ['exact']
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class ChecklistAreaType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = ChecklistAreas 
        interfaces = (relay.Node, )
        filter_fields = {
            'area': ['exact', 'icontains', 'istartswith'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id


class ChecklistType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = Checklist
        interfaces = (relay.Node, )
        filter_fields = {
            'message': ['exact', 'icontains', 'istartswith'],
            'area': ['exact'],
            'importance': ['exact'],
            'timeStampID': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class AccountNameType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = AccountName
        interfaces = (relay.Node, )
        filter_fields = {
            'id': ['exact'],
            'accountID': ['exact', 'icontains', 'istartswith'],
            'accountName': ['exact', 'icontains', 'istartswith'],
            'commonName': ['exact', 'icontains', 'istartswith'],
            'parentAccountID': ['exact'],
            'route': ['exact'],
            'productGroup': ['exact'],
            'accountDetails': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        # print('* * *', self.route)
        return self.id



# class MicroDeliveryRoutesType(ObjectType):
#     id = graphene.ID()
#     routeName = graphene.String()
#     loadingDay = graphene.Int()



    # def resolve_id(self, context, **kwargs):
    #     return self
    # def resolve_routeName(self, context, **kwargs):
    #     # item = (id=33, routeName="Please show me", loadingDay=4)
    #     item = {"id":"18", "routeName":"Please show me", "loadingDay":"4"}
    #     # print ('# #', item, json.dumps(item), json2obj(json.dumps(item)))
    #     # print ('* *', json2obj(json.dumps(item)))
    #     item2 = json2obj(json.dumps(item))

    #     # return item['routeName']
    #     return item2.routeName

# class ParentAccountNameType(ObjectType):
#     rowid = graphene.Int()
#     id = graphene.ID()
#     accountMRid = graphene.String()
#     commonName = graphene.String()
#     routeid = graphene.Field(MicroDeliveryRoutesType)
#     childAccount = graphene.List(lambda: ParentAccountNameType)

#     def resolve_rowid(self, context, **kwargs):
#         return self.id

#     def resolve_routeid(self, context, **kwargs):
#         return DeliveryRoutes.objects.get(id=self.routeid)

#     def resolve_childAccount(self, context, **kwargs):
#         url = 'http://192.168.2.25:8085/accounts/getChildrenOfParrentAccount/' + str(self.id)
#         data = requests.get(url)
#         data2 = json2obj(data.content)
#         data2 = json2obj(json.dumps(json.loads(data.content)))
#         return data2[:10]

# class MicroAccountNameType(ObjectType):
#     rowid = graphene.Int()
#     id = graphene.ID()
#     accountMRid = graphene.String()
#     commonName = graphene.String()
#     parentAccountid = graphene.Field(lambda: MicroAccountNameType)
#     # parentAccountid = graphene.Field(ParentAccountNameType)
#     routeid = graphene.Field(MicroDeliveryRoutesType)
#     productGroupid = graphene.Field(ProductGroupNameType)
#     accountDetails = graphene.String()
#     franchise = graphene.String()
    

#     def resolve_routeid(self, context, **kwargs):
#         return DeliveryRoutes.objects.get(id=self.routeid)

#     def resolve_productGroupid(self, context, **kwargs):
#         return Productgroupnames.objects.get(id=self.productGroupid)

#     def resolve_rowid(self, context, **kwargs):
#         return self.id

#     def resolve_parentAccountid(self, context, **kwargs):
#         if self.parentAccountid:
#             url = 'http://192.168.2.25:8085/accounts/getSingleAccount/' + str(self.parentAccountid)
#             data = requests.get(url)
#             data2 = json2obj(data.content)[0]
#             # print('! !', data2)
#             return data2

    # def resolve_parentAccountid(self, context, **kwargs):
    #     # if self.parentAccountid:
    #     #     url = 'http://192.168.2.25:8085/accounts/getSingleAccount/' + str(self.parentAccountid)
    #     #     data = requests.get(url)
    #     #     print('! !', json2obj(json.dumps(json.loads(data.content))))
    #     #     # return json2obj(json.dumps(json.loads(data.content)))
    #     #     return data.content
    #     # else:
    #     #     return None
    #     return json2obj(json.dumps([{"accountMRid":"HELLLOO!!"}]))

#     # X(id=510, accountMRid='V04', accountName='VLEISPALEIS', commonName='Vleis Paleis', routeid=14, productGroupid=2, accountAccessDBid=355, parentAccountid=None, accountDetails=[])


# class MicroAccountNameType(DjangoObjectType):
#     rowid = graphene.Int()
#     class Meta:
#         model = MicroSeriveAccountName
#         interfaces = (relay.Node, )
#         filter_fields = {
#             'id': ['exact'],
#             'accountMRid': ['exact', 'icontains', 'istartswith'],
#             'accountName': ['exact', 'icontains', 'istartswith'],
#             'commonName': ['exact', 'icontains', 'istartswith'],
#             'parentAccountid': ['exact'],
#             'routeid': ['exact'],
#             'productGroupid': ['exact'],
#             # 'accountDetails': ['exact'],
#             'accountAccessDBid': ['exact']
#         }
#     def resolve_rowid(self, context, **kwargs):
#         # print('* * *', self.route)
#         return self.id

class ReportImagesType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = ReportImages
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

# class OrderDetailsType(DjangoObjectType):
#     rowid = graphene.Int()
#     class Meta:
#         model = OrderDetails
#         interfaces = (relay.Node, )
#         filter_fields = {
#             'accountsid': ['exact'],
#             'accountMRid': ['exact', 'icontains', 'istartswith'],
#             'accountID': ['exact', 'icontains', 'istartswith'],
#             'commonName': ['exact', 'icontains', 'istartswith'],
#             'orderDate': ['exact'],
#             'timeStampid': ['exact'],
#             'routeid': ['exact'],
#             'delivered': ['exact'],
#         }
#     def resolve_rowid(self, context, **kwargs):
#         return self.id

# class OrderProductAmountsType(DjangoObjectType):
#     rowid = graphene.Int()
#     class Meta:
#         model = OrderProductAmounts
#         interfaces = (relay.Node, )
#         filter_fields = {
#             'orderDetailsid': ['exact'],
#             'productid': ['exact'],
#             'productMRid': ['exact', 'icontains', 'istartswith'],
#             'amount': ['exact', 'icontains', 'istartswith'],
#             'status': ['exact'],
#         }
#     def resolve_rowid(self, context, **kwargs):
#         return self.id

class Query(graphene.ObjectType):

    list_messageLevels = graphene.List(MessageLevelsType)
    list_dailyReport = graphene.List(DailyReportType)
    list_checklistAreas = graphene.List(ChecklistAreaType)

    # list_microAccountNames = graphene.List(MicroAccountNameType)
    # list_microDeliveryRoutes = graphene.List(MicroDeliveryRoutesType)
    # list_microParentAccount = graphene.List(ParentAccountNameType, id=Int(), accountMRid=String(), commonName=String())
    # list_micro_account_names_search = graphene.List(MicroAccountNameType, id=Int(), accountMRid=String(), commonName=String())

    node_messageLevels= DjangoFilterConnectionField(MessageLevelsType)
    node_dailyReport= DjangoFilterConnectionField(DailyReportType)
    node_checklistAreas = DjangoFilterConnectionField(ChecklistAreaType)
    node_checklist = DjangoFilterConnectionField(ChecklistType)
    node_accountNames = DjangoFilterConnectionField(AccountNameType)
    node_reportImages = DjangoFilterConnectionField(ReportImagesType)
    # node_orderDetails = DjangoFilterConnectionField(OrderDetailsType)
    # node_orderProductAmounts = DjangoFilterConnectionField(OrderProductAmountsType)


    def resolve_list_messageLevels(self, context, **kwargs):
        return MessageLevels.objects.all()

    def resolve_list_checklistAreas(self, context, **kwargs):
        return ChecklistAreas.objects.all()

    # def resolve_list_microAccountNames(self, context, *args, **kwargs):
    #     url = ACCOUNT_SERVICE_URL + GET_ALL_ACCOUNTS
    #     data = requests.get(url)
    #     # print('* *', json2obj(json.dumps(json.loads(data.content))))
    #     return json2obj(json.dumps(json.loads(data.content)))

    # def resolve_list_micro_account_names_search(self, context, *args, **kwargs):
    #     id = kwargs.get('id')
    #     accountMRid = kwargs.get('accountMRid')
    #     commonName = kwargs.get('commonName')
    #     if id is not None:
    #         url = ACCOUNT_SERVICE_URL + GET_SINGLE_ACCOUNT_ID + str(id)
    #         data = requests.get(url)
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     elif accountMRid is not None:
    #         url = ACCOUNT_SERVICE_URL + GET_SINGLE_ACCOUNT_MRID + str(accountMRid)
    #         data = requests.get(url)
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     if commonName is not None:
    #         url = ACCOUNT_SERVICE_URL + SEARCH_ACCOUNT_COMMONNAMES + str(commonName)
    #         data = requests.get(url)
    #         # print('* *', json2obj(json.dumps(json.loads(data.content))))
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     return None

    # def resolve_list_microParentAccount(self, context, *args, **kwargs):
    #     return json2obj(json.dumps({"data":{"accountMRid":"HELLLOO 1", "id":"3"}}))

    # def resolve_list_microParentAccount(self, context, *args, **kwargs):
    #     id = kwargs.get('id')
    #     accountMRid = kwargs.get('accountMRid')
    #     commonName = kwargs.get('commonName')
    #     # print('* = ', accountMRid)
    #     if id is not None:
    #         url = ACCOUNT_SERVICE_URL + GET_SINGLE_ACCOUNT_ID + str(id)
    #         data = requests.get(url)
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     elif accountMRid is not None:
    #         url = ACCOUNT_SERVICE_URL + GET_SINGLE_ACCOUNT_MRID + str(accountMRid)
    #         data = requests.get(url)
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     elif commonName is not None:
    #         url = ACCOUNT_SERVICE_URL + SEARCH_ACCOUNT_COMMONNAMES + str(commonName)
    #         data = requests.get(url)
    #         return json2obj(json.dumps(json.loads(data.content)))
    #     return None

    # def resolve_list_microDeliveryRoutes(self, context, **kwargs):
    #     print('# # ', context)
    #     return json2obj(json.dumps({"data":{"routeName":"HELLLOO 1", "id":"3"}}))

    # def resolve_time_stamp_filter(self, context, **kwargs):
    #     id = kwargs.get('id')
    #     if id is not None:
    #         return TimeStamp.objects.get(pk=id)
    #     return None








    # def resolve_list_microAccountNames(self, context, **kwargs):
    #     url = 'http://192.168.2.25:8085/accounts/getAllAccounts/'
    #     # headers = {
    #     #     "Content-Type": "application/json"
    #     # }
    #     # return call_api(request, url=url, headers=headers)
    #     # return Response(requests.post(url, headers=headers, data=json.dumps(request.data)).json())
    #     data = requests.get(url)
    #     # response.content
    #     # parsed = json.loads(response.content)
    #     print("* * * * * = ", json.loads(data.content))
    #     # r=json.dumps(data).json()
    #     # print(r)
    #     # data = http://192.168.2.25:8085/accounts/getAllAccounts/
    #     # print(json2obj(json.dumps([{"accountMRid":"HELLLOO!!"}])))
    #     # print(r)
    #     return json2obj(json.dumps(json.loads(data.content)))
    #     # return json.dumps(data.content)
    #     # return json2obj(json.dumps(data.content))
    #     # return json2obj(json.dumps([{"accountMRid":"HELLLOO 1"},{"accountMRid":"HELLLOO 2"}]))
    #     # return [{"accountMRid":"HELLLOO 1"},{"accountMRid":"HELLLOO 2"}]  # This jsut return accountMRids of null
    #     # ed['fk'] = base64.b64encode(bytes(fk, 'utf-8'))
    #     # ed['fk'] = base64.b64encode(bytes(fk, 'utf-8')).decode("ascii")