from django.db import models

class Packaging(models.Model):
    packagingType = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tbl_packaging'

class ProductBrands(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.brand

    class Meta: 
        managed = True
        db_table = 'tbl_productbrands'

class Batchgroups(models.Model):
    batchname = models.CharField(db_column='batchName', unique=True, max_length=255)  # Field name made lowercase.
    ranking = models.IntegerField(unique=True)

    def __str__(self):
        return self.batchname

    class Meta:
        managed = True
        db_table = 'tbl_batchgroups'

class Productlist(models.Model):
    productid = models.CharField(db_column='productID', unique=True, max_length=20)  # Field name made lowercase.
    proddescription = models.CharField(db_column='prodDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE, blank=True, null=True)
    unitweight = models.FloatField(db_column='unitWeight', blank=True, null=True)  # Field name made lowercase.
    packageweight = models.FloatField(db_column='packageWeight', blank=True, null=True)  # Field name made lowercase.
    productonhold = models.IntegerField(db_column='productOnHold', blank=True, null=True)  # Field name made lowercase.
    batchgroup = models.ForeignKey(Batchgroups, on_delete=models.CASCADE)
    batchranking = models.IntegerField(db_column='batchRanking', blank=True, null=True)  # Field name made lowercase.
    brand = models.ForeignKey(ProductBrands, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.productid

    class Meta:
        managed = True
        db_table = 'tbl_productlist'

class TblDeliveryroutes(models.Model):
    routes = models.CharField(unique=True, max_length=255)
    loadingday = models.IntegerField(db_column='loadingDay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbl_deliveryroutes'