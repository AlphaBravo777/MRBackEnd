from django.db import models
import datetime
from django.conf import settings

class HPPProductStatus(models.Model):
    productStatus = models.CharField(db_column='productStatus', max_length=255, blank=False, null=False)

    def __str__(self):
        return '%s' % (self.productStatus)

    class Meta:
        managed = True
        db_table = 'tbl_hppproductstatus'

class HPPMeatriteStock(models.Model):
    productid = models.ForeignKey('mrDatabaseModels.Productlist', db_column='productid', on_delete=models.CASCADE)
    batchNumberJunctionid = models.ForeignKey('mrDatabaseModels.ProductBatchNumbersJunction', db_column='batchNumberJunctionid', on_delete=models.CASCADE, null=False, blank=False)
    amount = models.IntegerField(db_column='amount')
    productStatusid = models.ForeignKey(HPPProductStatus, db_column='productStatusid', on_delete=models.CASCADE, null=False, blank=False)
    lastModified = models.DateTimeField(db_column='lastModified', auto_now=True, editable=False, null=True, blank=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='userid', on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return '%s %s %s' % (self.productid, self.productStatus, self.batchNumberJunctionid)

    class Meta:
        managed = True
        db_table = 'tbl_hppmeatritestock'
