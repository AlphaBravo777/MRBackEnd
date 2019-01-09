import graphene
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene import Node, ObjectType
from graphene import relay
from graphene import ID, String, Int, List
from django.db.models import Q

from .models import SettingsDB, FormBuilder, Forms, FormBuilderExtras
from django.contrib.auth.models import User

class SettingsDBType(DjangoObjectType):
    class Meta:
        model = SettingsDB 
        interfaces = (relay.Node, )
        filter_fields = {
            'settingName': ['exact', 'icontains', 'istartswith'],
        }

class UserType(DjangoObjectType):
    rowid = graphene.Int()
    class Meta:
        model = User 
        interfaces = (relay.Node, )
        filter_fields = {
        }
    def resolve_rowid(self, context, **kwargs):
        return self.id
    
class FormsType(DjangoObjectType):
    class Meta:
        model = Forms 
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }

class FormBuilderType(DjangoObjectType):
    class Meta:
        model = FormBuilder 
        interfaces = (relay.Node, )
        filter_fields = {
            'form': ['exact'],
            'type': ['exact', 'icontains', 'istartswith'],
            'name': ['exact', 'icontains', 'istartswith'],
            'label': ['exact', 'icontains', 'istartswith'],
            'value': ['exact', 'icontains', 'istartswith'],
            'placeholder': ['exact', 'icontains', 'istartswith'],
            'validation': ['exact'],
        }

class FormBuilderExtrasType(DjangoObjectType):
    class Meta:
        model = FormBuilderExtras
        interfaces = (relay.Node, )
        filter_fields = {
            'item': ['exact', 'icontains', 'istartswith'],
            'value': ['exact', 'icontains', 'istartswith'],
            'number': ['exact'],
        }

class Query(graphene.ObjectType):

    list_settingsDB = graphene.List(SettingsDBType)
    list_users = graphene.List(UserType)

    node_settingsDB = DjangoFilterConnectionField(SettingsDBType)
    node_users = DjangoFilterConnectionField(UserType)
    node_forms = DjangoFilterConnectionField(FormsType)
    node_formBuilder = DjangoFilterConnectionField(FormBuilderType)
    node_formBuilderExtras = DjangoFilterConnectionField(FormBuilderExtrasType)

    def resolve_list_settingsDB(self, context, **kwargs):
        return SettingsDB.objects.all()