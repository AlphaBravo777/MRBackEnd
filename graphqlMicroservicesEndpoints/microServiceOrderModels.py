from django.db import models
from mrDatabaseModels.models import TimeStamp, DeliveryRoutes
import uuid
import random

# If a model has a field that is a foreignKey to another model, then the modelSet (graphQL) will only show up in the other model.
# This means that the model that has the foreignKey will not have a modelSet available in its options
# The other minimum that you need is to have an objectType defined in the shema for the model, but you do not have to set a node_something(objectType)
# However, if you do not have a node_something(objectType), then you can not start with the model. It will not be available as your first query option
# So basically, to get a set for a shema, that shema does not have to know anything about the set
# You also do not need the model even to be in the database yet. So it does not care if the database is showing the field as a foreignkey (Just 
# created a model that showed up as a set without even migrating it)

class OrderDetailsMicroService(models.Model):

    accountid = models.PositiveSmallIntegerField(db_column='accountid', blank=False, null=False)
    accountMRid = models.CharField(db_column='accountMRid', unique=False, max_length=10, blank=False, null=False )
    commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
    orderDate = models.DateField(db_column='orderDate') # You can enter this just the way that it is, and it should accept it as a date : 2019-02-222
    timeStampid = models.PositiveSmallIntegerField(db_column='timeStampid', null=False, blank=False, unique=False)
    # timeStampid = models.ForeignKey('mrDatabaseModels.TimeStamp', db_column='timeStampid', on_delete=models.CASCADE, null=False, blank=False, unique=False)
    dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
    lastModified = models.DateTimeField(db_column='lastModified', auto_now=True, editable=False, null=True, blank=True)
    userid = models.PositiveSmallIntegerField(db_column='userid', null=False, blank=False)
    routeid = models.PositiveSmallIntegerField(db_column='routeid', blank=False, null=False)
    delivered = models.BooleanField(db_column='delivered', default=False)
    orderNumber = models.CharField(db_column='orderNumber', unique=False, max_length=100, blank=False, null=False, default=str(random.randint(1,1000000)))

    def __str__(self):
        return '%s %s' % (self.accountMRid, self.commonName)

    class Meta:

        # In order that this model does not get migrated with the rest of the other app models, we do not insert this app in the 'INSTALLED_APPS'
        # array, but the we have to add the "app_label" field in order for the program not to give an error
        app_label = 'orderDetailsMicroService'
        managed = False
        db_table = 'tbl_orderDetails'

class OrderProductAmountsMicroService(models.Model):
    orderDetailsid = models.ForeignKey(OrderDetailsMicroService, on_delete=models.CASCADE, db_column='orderDetailsid', blank=False, null=False)
    productid = models.PositiveSmallIntegerField(db_column='productid', blank=False, null=False)
    productMRid = models.CharField(db_column='productMRid', unique=False, max_length=20, blank=False, null=False )
    amount = models.IntegerField(db_column='amount')
    status = models.BooleanField(db_column='status', default=False)
    lastModified = models.DateTimeField(db_column='lastModified', auto_now=True, editable=False, null=True, blank=True)
    userid = models.PositiveSmallIntegerField(db_column='userid', null=False, blank=False)
    packageWeight = models.FloatField(db_column='packageWeight', blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.orderDetailsid, self.productMRid, self.amount)

    class Meta:
        app_label = 'orderDetailsMicroService'
        managed = False
        db_table = 'tbl_orderProductAmounts'

class TestForSETS(models.Model):
    productid = models.PositiveSmallIntegerField(db_column='productid', blank=False, null=False)
    orderDetailsid = models.ForeignKey(OrderDetailsMicroService, on_delete=models.CASCADE, db_column='orderDetailsid', blank=False, null=False)
    product = models.ForeignKey(OrderProductAmountsMicroService, on_delete=models.CASCADE, db_column='product', blank=False, null=False)
    route = models.ForeignKey(DeliveryRoutes, on_delete=models.CASCADE, db_column='route', blank=False, null=False)

    def __str__(self):
            return '%s' % (self.productid)

    class Meta:
        app_label = 'productid'
        managed = False
        db_table = 'tbl_productid'