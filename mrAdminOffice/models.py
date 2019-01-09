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
    accountID = models.CharField(db_column='accountID', unique=True, max_length=10, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
    parentAccountID = models.ForeignKey('self', on_delete=models.CASCADE, db_column='parentAccountID', blank=True, null=True)
    route = models.ForeignKey('mrDatabaseModels.DeliveryRoutes', on_delete=models.CASCADE, db_column='route', blank=False, null=False, default=1)
    productGroup = models.ForeignKey('mrDatabaseModels.Productgroupnames', on_delete=models.CASCADE, db_column='productGroup', blank=False, null=False, default=1)
    accountDetails = models.ManyToManyField(AccountDetails, through='AccountDetailsJunction')
    
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