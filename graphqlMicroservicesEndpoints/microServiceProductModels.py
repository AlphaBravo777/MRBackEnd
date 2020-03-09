from django.db import models
import datetime
from django.conf import settings

# -----------------------------------------------------------------------------------------------------------------------------------
class MeasuringUnit(models.Model): # What units can be used to measure an item, and how does the unit convert
# -----------------------------------------------------------------------------------------------------------------------------------
    unit = models.CharField(max_length=20, db_column='unit', null=False, \
        help_text='Any unit that a product or item can be measure in like g, kg, lt, ml, barrel, roll')
    convertionToMainUnitAmount = models.FloatField(db_column='convertionToMainUnitAmount', null=False, \
        help_text='What should this unit be multiplied with to make it the same value as if it was measured in its main unit')
    mainUnit = models.ForeignKey('self', db_column='mainUnit', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='What is the main unit that this unit will be converted to for measurements')

    def __str__(self):
        return f'{self.unit}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_measuringUnit'
        # ordering = ['unit']

# -----------------------------------------------------------------------------------------------------------------------------------
class ItemVendor(models.Model): # What units can be used to measure an item, and how does the unit convert
# -----------------------------------------------------------------------------------------------------------------------------------
    name = models.CharField(max_length=100, db_column='name', null=False, \
        help_text='The name of the vendor that produced the item')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_itemVendor'
        ordering = ['name']


# -----------------------------------------------------------------------------------------------------------------------------------
class Packaging(models.Model): # The type of packaging that an item can come in
# -----------------------------------------------------------------------------------------------------------------------------------
    packaging = models.CharField(max_length=20, db_column='packaging', null=False, \
        help_text='The final packaging that the unit/s are in now. Maybe a crate or box for groups or vacuum for a single packet')
    weight = models.PositiveSmallIntegerField(db_column='weight', null=True, \
        help_text='The weight of a crate or lug, to calculate for the weight of the truck')

    def __str__(self):
        return f'{self.packaging}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_packaging'
        ordering = ['packaging']

# -----------------------------------------------------------------------------------------------------------------------------------
class Item(models.Model): # The main table containing every item that can be found in the company from every department
# -----------------------------------------------------------------------------------------------------------------------------------
    name = models.CharField(db_column='name', max_length=255, null=False, blank=False, \
        help_text='The name or description of the item')
    size = models.FloatField(db_column='size', null=False, \
        help_text='The official size of the item (can only containe numbers like 2, 1000, 0.5)')
    unit = models.ForeignKey(MeasuringUnit, db_column='unit', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='Any unit that a product or item can be measured in like g, kg, lt, ml, barrel, roll') # Make sure the UnitMeasurements class has a conversion field to the main unit and main unit name maybe
    active = models.BooleanField(db_column='active', null=False, blank=False, \
        help_text='Is the item active at the moment or is it on hold? True = active, False = on_hold')
    packaging = models.ForeignKey(Packaging, db_column='packaging', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The outer most packaging that the item is in: box, crate, vacuum')
    price = models.DecimalField(db_column='price', max_digits=8, decimal_places=2,
        help_text='How much does the item officially cost')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_item'
        ordering = ['name']

# -----------------------------------------------------------------------------------------------------------------------------------
class ItemBuildingBlocks(models.Model): # The buildingblocks/ingredients that some items are made-up off
# -----------------------------------------------------------------------------------------------------------------------------------
    itemid = models.ForeignKey(Item, db_column='itemid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The main item that are made-up of the building blocks')
    buildingBlock = models.ForeignKey(Item, db_column='buildingBlock', related_name='buildingBlock', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='Building block that goes into creating this item')
    quantity = models.PositiveSmallIntegerField(db_column='quantity', null=False, blank=False, \
        help_text='The quantity of the building block that goes into the item')

    def __str__(self):
        return f'{self.itemid} // {self.buildingBlock}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_itemBuildingBlocks'
        ordering = ['itemid']

# -----------------------------------------------------------------------------------------------------------------------------------
class CalculatedPrice(models.Model): # Some items gets their prices from others, and it get documented here
# -----------------------------------------------------------------------------------------------------------------------------------
    itemid = models.ForeignKey(Item, db_column='itemid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The item which price needs to be calculated')
    priceSource = models.ForeignKey(Item, db_column='priceSource', related_name='priceSource', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The item from which the price must be calculated from')
    modifier = models.PositiveSmallIntegerField(db_column='modifier', null=True, \
        help_text='What should the priceSource price be mulitplied with to get the current price.')

    def __str__(self):
        return f'{self.itemid} // {self.priceSource}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_calculatedPrice'
        ordering = ['itemid']

# -----------------------------------------------------------------------------------------------------------------------------------
class Department(models.Model): # The departments that are available where items can be accessed
# -----------------------------------------------------------------------------------------------------------------------------------   
    name = models.CharField(db_column='name', max_length=255, null=False, blank=False, \
        help_text='The name of the department')
    rankingInDepartment = models.PositiveSmallIntegerField(db_column='rankingInDepartment', blank=True, null=True, \
        help_text='The ranking that this department has when listed compared to the other departments')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_department'
        ordering = ['rankingInDepartment']

# -----------------------------------------------------------------------------------------------------------------------------------
class Category(models.Model): # All the categories that are found in a department
# -----------------------------------------------------------------------------------------------------------------------------------   
    name = models.CharField(db_column='name', max_length=255, null=False, blank=False, \
        help_text='The name of the the catagory')
    rankingInCategory = models.PositiveSmallIntegerField(db_column='rankingInCategory', blank=True, null=True, \
        help_text='The ranking that this category has when listed compared to the other categories')
    departmentid = models.ForeignKey(Department, db_column='departmentid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The department where this catagory shows up')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_category'
        ordering = ['rankingInCategory']

# -----------------------------------------------------------------------------------------------------------------------------------
class Group(models.Model): # All the categories that are found in a department
# -----------------------------------------------------------------------------------------------------------------------------------   
    name = models.CharField(db_column='name', max_length=255, null=False, blank=False, \
        help_text='The name of the group that this product can fall into')
    rankingInGroup = models.PositiveSmallIntegerField(db_column='rankingInGroup', blank=True, null=True, \
        help_text='The ranking that this group has when listed compared to the other groups')
    categoryid = models.ForeignKey(Category, db_column='categoryid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The catagory where this group shows up')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_group'
        ordering = ['rankingInGroup']

# -----------------------------------------------------------------------------------------------------------------------------------
class ItemGrouping(models.Model): # Records of every department where the item shows up, and its id for that department
# -----------------------------------------------------------------------------------------------------------------------------------
    itemid = models.ForeignKey(Item, db_column='itemid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The item which pertains to this group and department description')
    departmentid = models.ForeignKey(Department, db_column='departmentid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The department where this catagory shows up')
    catagoryid = models.ForeignKey(Category, db_column='catagoryid', related_name='catagoryid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The catagory where this group shows up')
    groupid = models.ForeignKey(Group, db_column='groupid', null=False, blank=False, on_delete=models.CASCADE, \
        help_text='The group where this item shows up')
    itemCode = models.CharField(db_column='itemCode', max_length=40, null=False, blank=False, \
        help_text='The code of the item that will show at this department')

    def __str__(self):
        return f'{self.itemid} -> {self.departmentid} -> {self.catagoryid} -> {self.groupid} -> {self.itemCode}'

    class Meta:
        app_label = 'productMicroService'
        managed = False
        db_table = 'tbl_itemGrouping'
        ordering = ['itemid']
