import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List
from django.db.models import Q

from .models import MessageLevels, DailyReport, ChecklistAreas, Checklist, AccountName
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
            'accountName': ['exact', 'icontains', 'istartswith'],
            'commonName': ['exact', 'icontains', 'istartswith'],
            'parentAccountID': ['exact'],
            'route': ['exact'],
            'productGroup': ['exact'],
            'accountDetails': ['exact'],
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

    def resolve_list_messageLevels(self, context, **kwargs):
        return MessageLevels.objects.all()

    def resolve_list_checklistAreas(self, context, **kwargs):
        return ChecklistAreas.objects.all()