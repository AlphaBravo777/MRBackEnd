# This may be where you import all the different models to combine them into one

import graphene

import mrDatabaseModels.schema as Database
import mrCoreModels.schema as Core
import mrAdminOffice.schema as Office

class Query(Database.Query, Core.Query, Office.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass

schema = graphene.Schema(query=Query)