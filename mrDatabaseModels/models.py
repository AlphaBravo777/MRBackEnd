from django.db import models
import datetime
from django.conf import settings

class StockTakingTimes(models.Model):
    times = models.CharField(unique=True, max_length=255)
    selectiveDelete = models.BooleanField(db_column='selectiveDelete', default=False)

    def __str__(self):
        return self.times

    class Meta:
        managed = True
        db_table = 'tbl_stocktakingtimes'

class DaysOfTheWeek(models.Model):
    weekDayNames = models.CharField(db_column='weekDayNames', blank=False, unique=True, max_length=100)
    weekDayNumber = models.IntegerField(db_column='weekDayNumber', blank=False, unique=True, null=False)
    weekDayRanking = models.IntegerField(db_column='weekDayRanking', blank=False, unique=True, null=False)

    def __str__(self):
        return self.weekDayNames

    class Meta:
        managed = True
        db_table = 'tbl_daysoftheweek'

class DeliveryRoutes(models.Model):
    routeName = models.CharField(db_column='routeName', blank=False, null=False, unique=True, max_length=255)
    loadingDay = models.ForeignKey(DaysOfTheWeek, on_delete=models.CASCADE, db_column='loadingDay', blank=False, null=False, default=1)

    def __str__(self):
        return self.routeName

    class Meta:
        managed = True
        db_table = 'tbl_deliveryroutes'

class Shifts(models.Model):
    shiftName = models.CharField(db_column='shiftName', blank=False, null=False, unique=True, max_length=100)
    shiftSuperVisor = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='shiftSuperVisor', on_delete=models.CASCADE, null=True, blank=True, default=23)

    def __str__(self):
        return self.shiftName

    class Meta:
        managed = True
        db_table = 'tbl_shifts'

class TimeStamp(models.Model):
    year = models.IntegerField(db_column='year', blank=False, null=False, default=2018)
    week = models.IntegerField(db_column='week', blank=False, null=False, default=1)
    weekDay = models.ForeignKey('DaysOfTheWeek', on_delete=models.CASCADE, db_column='weekDay', blank=False, null=False, default=1)
    time = models.ForeignKey(StockTakingTimes, db_column='time', on_delete=models.CASCADE, blank=False, unique=False, default=1)
    shortDate = models.DateField(db_column='shortDate', blank=False, unique=False, default=datetime.date.today)
    dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
    shift = models.ForeignKey(Shifts, db_column='shift', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        # return str(self.year)
        return '%s %s %s %s %s' % (self.year, self.week, self.weekDay, self.shift, self.time)

    class Meta: 
        managed = True
        db_table = 'tbl_timestamp'

class Packaging(models.Model):
    packaging_type = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.packaging_type

    class Meta: 
        managed = True
        db_table = 'tbl_packaging'

class Image(models.Model):
    imageName = models.CharField(max_length=255, blank=True, null=True)
    imageDescription = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.imageName

    class Meta:
        managed = True
        db_table = 'tbl_image'

class ProductBrands(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    brandSmallImage = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.brand

    class Meta: 
        managed = True
        db_table = 'tbl_productbrands'

class ColorCodes(models.Model):
    itemDescription = models.CharField(db_column='itemDescription', max_length=100)  # Field name made lowercase.
    colorCode = models.CharField(db_column='colorCode', max_length=201)

    def __str__(self):
        return self.itemDescription 

    class Meta:
        managed = True
        db_table = 'tbl_colorcodes'

class MeasuringUnits(models.Model):
    unitAmount = models.DecimalField(db_column='unitAmount', decimal_places=3, max_digits=10, null=False, blank=False)  # Field name made lowercase.
    measuringUnit = models.CharField(db_column='measuringUnit', max_length=100)
    unitColor = models.ForeignKey(ColorCodes, db_column='unitColor', on_delete=models.CASCADE, blank=True, null=True)
    unitDescription = models.CharField(db_column='unitDescription', max_length=100)
    unitImage = models.ForeignKey(Image, db_column='unitImage', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.unitAmount)

    class Meta:
        managed = True
        db_table = 'tbl_measuringunits'

class Batchgroups(models.Model):
    batchname = models.CharField(db_column='batchName', unique=True, max_length=100)  # Field name made lowercase.
    ranking = models.IntegerField(unique=True)
    packingListRanking = models.IntegerField(unique=True, blank=True, null=True)
    batchColor = models.ForeignKey(ColorCodes, db_column='batchColor', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.batchname

    class Meta:
        managed = True
        db_table = 'tbl_batchgroups'

class Productlist(models.Model):
    productid = models.CharField(unique=True, db_column='productid', max_length=20)  # Field name made lowercase.
    proddescription = models.CharField(db_column='proddescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    packaging = models.ForeignKey(Packaging, db_column='packaging', on_delete=models.CASCADE, blank=True, null=True)
    unitweight = models.ForeignKey(MeasuringUnits, db_column='unitweight', null=True, blank=True, on_delete=models.CASCADE)
    packageweight = models.FloatField(db_column='packageweight', blank=True, null=True)  # Field name made lowercase.
    productonhold = models.BooleanField(db_column='productonhold', default=False)
    batchgroup = models.ForeignKey(Batchgroups, db_column='batchgroup', on_delete=models.CASCADE)
    stocktakegroup = models.ForeignKey(Batchgroups, db_column='stocktakegroup', on_delete=models.CASCADE, related_name='stocktakegroup', default=1)
    batchranking = models.IntegerField(db_column='batchranking', blank=True, null=True)  # Field name made lowercase.
    brand = models.ForeignKey(ProductBrands, db_column='brand', on_delete=models.CASCADE, blank=True, null=True)
    packlistgroup = models.ForeignKey(Batchgroups, db_column='packlistgroup', on_delete=models.CASCADE, related_name='packlistgroup', default=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE, null=False, blank=False, default=23)
    brandImage = models.ForeignKey(Image, db_column='brandImage', on_delete=models.CASCADE, blank=True, null=True, default=19)
    rankingInGroup = models.IntegerField(db_column='rankingInGroup', blank=True, null=True)

    def __str__(self):
        return self.productid

    class Meta:
        managed = True
        db_table = 'tbl_productlist'
        ordering = ['productid']  #Default ordering

class ProcessedStockAmounts(models.Model):
    prodName = models.ForeignKey(Productlist, db_column='prodName', on_delete=models.CASCADE, blank=False, unique=False)
    container = models.ForeignKey('Productcontainernames', db_column='container', on_delete=models.CASCADE, blank=False, unique=False, default=1)
    amount = models.CharField(unique=False, max_length=10)
    time = models.ForeignKey(StockTakingTimes, db_column='time', on_delete=models.CASCADE, blank=False, unique=False, default=1)
    timeStampID = models.ForeignKey(TimeStamp, db_column='timeStampID', on_delete=models.CASCADE, blank=False, unique=False, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='user', on_delete=models.CASCADE, null=False, blank=False, default=23)
    dateCreated = models.DateTimeField(auto_now_add=True, db_column='dateCreated', editable=False, null=True, blank=True)
    prodContainer= models.ForeignKey('Productcontainers', db_column='prodContainer', on_delete=models.CASCADE, blank=False, unique=False, default=1)

    def __str__(self):
        return str(self.prodName)

    class Meta:
        managed = True
        db_table = 'tbl_processedstockamounts'


class Productgroupnames(models.Model):
    groupname = models.CharField(db_column='groupName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    group = models.CharField(max_length=255, blank=True, null=True)
    grouprating = models.IntegerField(db_column='groupRating', blank=True, null=True)  # Field name made lowercase.
    members = models.ManyToManyField(Productlist, through='Productgroups')

    def __str__(self):
        return self.groupname

    class Meta:
        managed = True
        db_table = 'tbl_productgroupnames'

class Productgroups(models.Model):
    groupnameid = models.ForeignKey(Productgroupnames, on_delete=models.CASCADE) 
    productid = models.ForeignKey(Productlist, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.groupnameid) + ' ' + str(self.productid)

    class Meta:
        managed = True
        db_table = 'tbl_productgroups'

class Productcontainernames(models.Model):
    containername = models.CharField(db_column='containerName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    members = models.ManyToManyField(Productlist, through='Productcontainers')

    def __str__(self):
        return self.containername

    class Meta:
        managed = True
        db_table = 'tbl_productcontainernames'

class Factoryarea(models.Model):
    area = models.CharField(db_column='area', max_length=255, blank=False, null=False, unique=True)
    areaRanking = models.IntegerField(db_column='areaRanking',unique=False, blank=False, null=False)

    def __str__(self):
        return self.area

    class Meta:
        managed = True
        db_table = 'tbl_factoryarea'

class Factorysubarea(models.Model):
    area = models.ForeignKey(Factoryarea, db_column='area', on_delete=models.CASCADE, blank=True, null=True)
    subArea = models.CharField(db_column='subArea', max_length=255, blank=False, null=False, unique=True)
    subAreaRanking = models.IntegerField(db_column='subAreaRanking',unique=False, blank=False, null=False)

    def __str__(self):
        return self.section

    class Meta:
        managed = True
        db_table = 'tbl_factorysubarea'
    
class Productcontainers(models.Model):
    containernameid = models.ForeignKey(Productcontainernames, db_column='containernameid', on_delete=models.CASCADE) 
    productid = models.ForeignKey(Productlist, db_column='productid', on_delete=models.CASCADE) 
    deleteContainerAmount = models.BooleanField(default=True)
    factoryRanking = models.IntegerField(db_column='factoryranking', blank=True, null=True)
    factorySubArea = models.ForeignKey(Factorysubarea, db_column='factorySubArea', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ForeignKey(Image, db_column='image', on_delete=models.CASCADE, blank=True, null=True)
    filterCatagory = models.ForeignKey(Factoryarea, db_column='filterCatagory', on_delete=models.CASCADE, blank=True, null=True)
    factoryCatagory = models.ForeignKey(Factoryarea, related_name='Factoryarea_factoryCatagory', db_column='factoryCatagory', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.productid) + ' ' + str(self.containernameid) 

    class Meta:
        managed = True
        db_table = 'tbl_productcontainers'

class HighRiskPackingList(models.Model):
    productCode = models.OneToOneField(Productlist, db_column='productCode', on_delete=models.CASCADE, primary_key=True) 
    currentStock = models.IntegerField(db_column='currentStock', blank=False, null=False)
    stockNeeded = models.IntegerField(db_column='stockNeeded', blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False, default=23)
    # created = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    # last_modified = models.DateTimeField(auto_now=True, editable=False, null=True, blank=True)

    def __str__(self):
        return str(self.productCode)

    class Meta:
        managed = True
        db_table = 'tbl_highriskpackinglist'
        ordering = ['productCode']  #Default ordering

class BatchNumbers(models.Model):
    batchMRid = models.CharField(db_column='batchMRid', max_length=255, blank=False, null=False, unique=True)
    cleared = models.BooleanField(db_column='cleared', default=True)
    batchGroup = models.ManyToManyField(Batchgroups, through='ProductBatchNumbersJunction')

    def __str__(self):
        return str(self.batchMRid)

    class Meta:
        managed = True
        db_table = 'tbl_batchnumbers'
        ordering = ['batchMRid']  #Default ordering

class ProductBatchNumbersJunction(models.Model):
    batchGroup = models.ForeignKey(Batchgroups, db_column='batchGroup', on_delete=models.CASCADE) 
    batchNumbers = models.ForeignKey(BatchNumbers, db_column='batchNumbers', on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.batchGroup) + ' ' + str(self.batchNumbers)

    class Meta:
        managed = True
        db_table = 'tbl_productbatchnumbersjunction'

class MeatriteStock(models.Model):

    productid = models.ForeignKey(Productlist, db_column='productid', on_delete=models.CASCADE)
    batchNumberJunctionid = models.ForeignKey(ProductBatchNumbersJunction, db_column='batchNumberJunctionid', on_delete=models.CASCADE, null=False, blank=False) 
    amount = models.IntegerField(db_column='amount', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, db_column='created', editable=False, null=True, blank=True)
    lastModified = models.DateTimeField(auto_now=True, db_column='lastModified',  editable=False, null=True, blank=True)
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, db_column='userid', on_delete=models.CASCADE, null=False, blank=False, default=23)

    def __str__(self):
        return str(self.productid) + ' ' + str(self.batchNumberJunctionid)

    class Meta:
        managed = True
        db_table = 'tbl_meatritestock'




# * amount: 5
# * batchNumberJunctionid: 50
# batchGroupid: 2
# batchNumber: "09:4"
# * productid: 127
# * userid: 15


# mysql -u root -p

# SELECT table_name AS "Table",
# ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size (MB)"
# FROM information_schema.TABLES
# WHERE table_schema = "meatritedb"
# ORDER BY (data_length + index_length) DESC;

# ProcessedStockAmounts size at 2018/11/21 = 0.39m