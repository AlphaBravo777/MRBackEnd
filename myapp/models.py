from django.db import models

class TblProductlist(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.CharField(db_column='productID', unique=True, max_length=20)  # Field name made lowercase.
    proddescription = models.CharField(db_column='prodDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packaging = models.IntegerField(blank=True, null=True)
    unitweight = models.FloatField(db_column='unitWeight', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'tbl_productlist'

class ApiBucketlist(models.Model):
    name = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'api_bucketlist'