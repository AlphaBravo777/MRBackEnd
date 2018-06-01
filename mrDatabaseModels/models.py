from django.db import models

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
    packaging = models.IntegerField(blank=True, null=True)
    unitweight = models.FloatField(db_column='unitWeight', blank=True, null=True)  # Field name made lowercase.
    packageweight = models.FloatField(db_column='packageWeight', blank=True, null=True)  # Field name made lowercase.
    productonhold = models.IntegerField(db_column='productOnHold', blank=True, null=True)  # Field name made lowercase.
    batchgroup = models.ForeignKey(Batchgroups, on_delete=models.CASCADE)
    batchranking = models.IntegerField(db_column='batchRanking', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.productid

    class Meta:
        managed = True
        db_table = 'tbl_productlist'
