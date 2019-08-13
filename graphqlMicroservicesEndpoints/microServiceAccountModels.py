from django.db import models
import datetime
from django.conf import settings

class Franchise(models.Model):
    franchiseName = models.CharField(db_column='franchiseName', unique=True, max_length=255, blank=False, null=False)
    
    def __str__(self):
        return '%s' % (self.franchiseName)

    class Meta: 
        app_label = 'accountDetailsMicroService'
        managed = False
        db_table = 'tbl_franchise'

class AccountDetails(models.Model):
    detailsName = models.CharField(db_column='detailsName', unique=False, max_length=255, blank=False, null=False )
    phoneNumber = models.CharField(db_column='phoneNumber', unique=False, max_length=20, blank=True, null=True )
    contactPerson = models.CharField(db_column='contactPerson', unique=False, max_length=255, blank=True, null=True )
    address = models.CharField(db_column='address', unique=False, max_length=255, blank=True, null=True )
    
    def __str__(self):
        return '%s' % (self.detailsName)

    class Meta: 
        app_label = 'accountDetailsMicroService'
        managed = False
        db_table = 'tbl_accountDetails'

class AccountName(models.Model):
    accountMRid = models.CharField(db_column='accountMRid', unique=False, max_length=10, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
    parentAccountid = models.ForeignKey('self', on_delete=models.CASCADE, db_column='parentAccountid', blank=True, null=True)
    routeid = models.PositiveSmallIntegerField(db_column='routeid', blank=False, null=False)
    productGroupid = models.PositiveSmallIntegerField(db_column='productGroupid', blank=False, null=False)
    accountDetails = models.ManyToManyField(AccountDetails, through='AccountDetailsJunction')
    accountAccessDBid = models.IntegerField(db_column='accountAccessDBid', null=True)
    franchise = models.ForeignKey(Franchise, on_delete=models.CASCADE, db_column='franchise', blank=False, null=False, default=1)
    
    
    def __str__(self):
        return '%s %s' % (self.accountMRid, self.commonName)

    class Meta: 
        app_label = 'accountDetailsMicroService'
        managed = False
        db_table = 'tbl_accountName'

class AccountDetailsJunction(models.Model):
    mrAccountid = models.ForeignKey(AccountName, db_column='mrAccountid', on_delete=models.CASCADE) 
    accountDetailsid = models.ForeignKey(AccountDetails, db_column='accountDetailsid', on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.mrAccountid) + ' ' + str(self.accountDetailsid)

    class Meta:
        app_label = 'accountDetailsMicroService'
        managed = False
        db_table = 'tbl_accountDetailsJunction'

