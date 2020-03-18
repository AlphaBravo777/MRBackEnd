# This may be where you import all the different models to combine them into one

import graphene

import mrDatabaseModels.schema as Database
import mrCoreModels.schema as Core
import mrAdminOffice.schema as Office
import mrStock.schema as Stock
import graphqlMicroservicesEndpoints.microServiceOrderSchema as OrderService
import graphqlMicroservicesEndpoints.microServiceAccountSchema as AccountService
import graphqlMicroservicesEndpoints.microServiceProductSchema as ProductService

class Query(Database.Query, Core.Query, Office.Query, Stock.Query, AccountService.Query, OrderService.Query, ProductService.Query, graphene.ObjectType):
    # This class extends all abstract apps level Queries and graphene.ObjectType
    pass

schema = graphene.Schema(query=Query)