from django.db import models
import datetime
from django.conf import settings

class AccountName(models.Model):
    accountID = models.CharField(db_column='accountID', unique=True, max_length=10, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    commonName = models.CharField(db_column='commonName', unique=False, max_length=255, blank=False, null=False )
    
    def __str__(self):
        return '%s %s' % (self.accountID, self.commonName)

    class Meta: 
        managed = True
        db_table = 'tbl_accountname'

class AccountChild(models.Model):
    mainAccount = models.ForeignKey(AccountName, on_delete=models.CASCADE, db_column='mainAccount', blank=False, null=False, default=1)
    childAccountID = models.CharField(db_column='ChildAccountID', max_length=20, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    
    def __str__(self):
        return '%s %s' % (self.childAccountID, self.accountName)

    class Meta: 
        managed = True
        db_table = 'tbl_accountchild'

class AccountGrandChild(models.Model):
    childAccount = models.ForeignKey(AccountChild, on_delete=models.CASCADE, db_column='childAccount', blank=False, null=False, default=1)
    grandChildAccountID = models.CharField(db_column='grandChildAccountID', max_length=50, blank=False, null=False )
    accountName = models.CharField(db_column='accountName', unique=False, max_length=255, blank=False, null=False )
    route = models.ForeignKey('mrDatabaseModels.DeliveryRoutes', on_delete=models.CASCADE, db_column='route', blank=False, null=False, default=1)
    productGroup = models.ForeignKey('mrDatabaseModels.Productgroupnames', on_delete=models.CASCADE, db_column='productGroup', blank=False, null=False, default=1)
    
    def __str__(self):
        return '%s %s' % (self.grandChildAccountID, self.accountName)

    class Meta: 
        managed = True
        db_table = 'tbl_accountgrandchild'

# class AccountDetails(models.Model):
#     accountid = models.OneToOneField(AccountName, db_column='accountid', on_delete=models.CASCADE, primary_key=True)
#     phoneNumber1 = models.CharField(db_column='phoneNumber1', unique=False, max_length=15, blank=True, null=True )
#     address = models.CharField(db_column='address', unique=False, max_length=255, blank=True, null=True )
    
#     def __str__(self):
#         return '%s' % (self.accountid)

#     class Meta: 
#         managed = True
#         db_table = 'tbl_accountdetails'

