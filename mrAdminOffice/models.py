from django.db import models
import datetime
from django.conf import settings

class AccountDetails(models.Model):
    detailsName = models.CharField(db_column='detailsName', unique=False, max_length=255, blank=False, null=False )
    phoneNumber = models.CharField(db_column='phoneNumber', unique=False, max_length=20, blank=True, null=True )
    contactPerson = models.CharField(db_column='contactPerson', unique=False, max_length=255, blank=True, null=True )
    address = models.CharField(db_column='address', unique=False, max_length=255, blank=True, null=True )
    
    def __str__(self):
        return '%s' % (self.detailsName)

    class Meta: 
        managed = True
        db_table = 'tbl_accountdetails'

class AccountName(models.Model):
    accountID = models.CharField(db_column='accountID', unique=False, max_length=10, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
    parentAccountID = models.ForeignKey('self', on_delete=models.CASCADE, db_column='parentAccountID', blank=True, null=True)
    route = models.ForeignKey('mrDatabaseModels.DeliveryRoutes', on_delete=models.CASCADE, db_column='route', blank=False, null=False, default=1)
    productGroup = models.ForeignKey('mrDatabaseModels.Productgroupnames', on_delete=models.CASCADE, db_column='productGroup', blank=False, null=False, default=1)
    accountDetails = models.ManyToManyField(AccountDetails, through='AccountDetailsJunction')
    accountAccessDBid = models.IntegerField(db_column='accountAccessDBid', null=True)
    
    def __str__(self):
        return '%s %s' % (self.accountID, self.commonName)

    class Meta: 
        managed = True
        db_table = 'tbl_accountname'

class AccountDetailsJunction(models.Model):
    accountID = models.ForeignKey(AccountName, db_column='accountID', on_delete=models.CASCADE) 
    accountDetailsID = models.ForeignKey(AccountDetails, db_column='accountDetailsID', on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.accountID) + ' ' + str(self.accountDetailsID)

    class Meta:
        managed = True
        db_table = 'tbl_accountdetailsjunction'

class MessageLevels(models.Model):
    levelName = models.CharField(db_column='levelName', max_length=100)
    levelColor = models.CharField(db_column='levelColor', max_length=100)
    levelRank = models.IntegerField(db_column='levelRank')
    report = models.BooleanField(db_column='report', default=False)
    checklist = models.BooleanField(db_column='checklist', default=False)

    def __str__(self):
        return '%s' % (self.levelName)

    class Meta:
        managed = True
        db_table = 'tbl_messagelevels'

class DailyReport(models.Model):
    message = models.TextField(db_column='message', blank=False, null=False)
    messageLevel = models.ForeignKey(MessageLevels, on_delete=models.CASCADE, db_column='messageLevel', blank=False, null=False, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE, null=False, blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
    timeStampID = models.ForeignKey('mrDatabaseModels.TimeStamp', db_column='timeStampID', on_delete=models.CASCADE, null=False, blank=False, unique=False, default=1)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, db_column='reply', blank=True, null=True)

    def __str__(self):
        return '%s' % (self.message)

    class Meta:
        managed = True
        db_table = 'tbl_dailyreport'

class ChecklistAreas(models.Model):
    area = models.CharField(db_column='area', max_length=100)
    
    def __str__(self):
        return '%s' % (self.area)

    class Meta:
        managed = True
        db_table = 'tbl_checklistareas'

class Checklist(models.Model):
    message = models.TextField(db_column='message', blank=False, null=False)
    area = models.ForeignKey(ChecklistAreas, on_delete=models.CASCADE, db_column='area', blank=False, null=False, default=1)
    importance = models.ForeignKey(MessageLevels, on_delete=models.CASCADE, db_column='importance', blank=False, null=False, default=1,  related_name='+')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE, null=False, blank=False)
    dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
    timeStampID = models.ForeignKey('mrDatabaseModels.TimeStamp', db_column='timeStampID', on_delete=models.CASCADE, null=False, blank=False, unique=False, default=1)


    def __str__(self):
        return '%s' % (self.message)

    class Meta:
        managed = True
        db_table = 'tbl_checklist'

class ReportImages(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="dailyReport/", null=False, blank=False)
    report = models.ForeignKey(DailyReport, on_delete=models.CASCADE, db_column='report', blank=False, null=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        managed = True
        db_table = 'tbl_reportimages'

# class OrderDetails(models.Model):
#     accountsid = models.ForeignKey(AccountName, on_delete=models.CASCADE, db_column='accountids', blank=False, null=False)
#     accountMRid = models.CharField(db_column='accountMRid', unique=False, max_length=4, blank=False, null=False )
#     accountID = models.CharField(db_column='accountID', unique=False, max_length=40, blank=False, null=False )
#     commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
#     orderDate = models.DateField(db_column='orderDate') # You can enter this just the way that it is, and it should accept it as a date : 2019-02-222
#     timeStampid = models.ForeignKey('mrDatabaseModels.TimeStamp', db_column='timeStampid', on_delete=models.CASCADE, null=False, blank=False, unique=False)
#     dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
#     lastModified = models.DateTimeField(db_column='lastModified', auto_now=True, editable=False, null=True, blank=True)
#     userid = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE, null=False, blank=False)
#     routeid = models.ForeignKey('mrDatabaseModels.DeliveryRoutes', on_delete=models.CASCADE, db_column='routeid', blank=False, null=False)
#     delivered = models.BooleanField(db_column='delivered', default=False)
#     orderNumber = models.CharField(db_column='orderNumber', unique=False, max_length=40, blank=True, null=True)
#     # accountAccessDBid = models.IntegerField(db_column='accountAccessDBid', unique=True, null=True)

#     def __str__(self):
#         return '%s %s' % (self.accountMRid, self.commonName)

#     class Meta:
#         managed = True
#         db_table = 'tbl_orderdetails'

# class OrderProductAmounts(models.Model):
#     orderDetailsid = models.ForeignKey(OrderDetails, on_delete=models.CASCADE, db_column='orderDetailsid', blank=False, null=False)
#     productid = models.ForeignKey('mrDatabaseModels.Productlist', on_delete=models.CASCADE, db_column='productid', blank=False, null=False)
#     productMRid = models.CharField(db_column='productMRid', unique=False, max_length=20, blank=False, null=False )
#     amount = models.IntegerField(db_column='amount')
#     status = models.BooleanField(db_column='status', default=False)
#     lastModified = models.DateTimeField(db_column='lastModified', auto_now=True, editable=False, null=True, blank=True)
#     userid = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='userid', on_delete=models.CASCADE, null=False, blank=False)

#     def __str__(self):
#         return '%s %s %s' % (self.orderDetailsid, self.productMRid, self.amount)

#     class Meta:
#         managed = True
#         db_table = 'tbl_orderproductamounts'