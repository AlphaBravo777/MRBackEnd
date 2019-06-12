import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List
from django.db.models import Q

from .models import MessageLevels, DailyReport, ChecklistAreas, Checklist, AccountName, ReportImages, OrderDetails, OrderProductAmounts

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
        return self.id

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

class OrderDetailsType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = OrderDetails
        interfaces = (relay.Node, )
        filter_fields = {
            'accountsid': ['exact'],
            'accountMRid': ['exact', 'icontains', 'istartswith'],
            'accountID': ['exact', 'icontains', 'istartswith'],
            'commonName': ['exact', 'icontains', 'istartswith'],
            'orderDate': ['exact'],
            'timeStampid': ['exact'],
            'routeid': ['exact'],
            'delivered': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class OrderProductAmountsType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = OrderProductAmounts
        interfaces = (relay.Node, )
        filter_fields = {
            'orderDetailsid': ['exact'],
            'productid': ['exact'],
            'productMRid': ['exact', 'icontains', 'istartswith'],
            'amount': ['exact', 'icontains', 'istartswith'],
            'status': ['exact'],
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id

class Query(graphene.ObjectType):

    list_messageLevels = graphene.List(MessageLevelsType)
    list_dailyReport = graphene.List(DailyReportType)
    list_checklistAreas = graphene.List(ChecklistAreaType)

    node_messageLevels= DjangoFilterConnectionField(MessageLevelsType)
    node_dailyReport= DjangoFilterConnectionField(DailyReportType)
    node_checklistAreas = DjangoFilterConnectionField(ChecklistAreaType)
    node_checklist = DjangoFilterConnectionField(ChecklistType)
    node_accountNames = DjangoFilterConnectionField(AccountNameType)
    node_reportImages = DjangoFilterConnectionField(ReportImagesType)
    node_orderDetails = DjangoFilterConnectionField(OrderDetailsType)
    node_orderProductAmounts = DjangoFilterConnectionField(OrderProductAmountsType)

    def resolve_list_messageLevels(self, context, **kwargs):
        return MessageLevels.objects.all()

    def resolve_list_checklistAreas(self, context, **kwargs):
        return ChecklistAreas.objects.all()