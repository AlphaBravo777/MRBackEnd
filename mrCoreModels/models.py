from django.db import models
import datetime
from django.conf import settings

class SettingsDB(models.Model):
    settingName = models.CharField(db_column='settingName', max_length=255)
    value1 = models.CharField(db_column='value1', max_length=255)
    value2 = models.CharField(db_column='value2', max_length=255)

    def __str__(self):
        return '%s %s' % (self.settingName, self.value1)

    class Meta:
        managed = True
        db_table = 'tbl_settingsdb'

# Main name of every form, this gets used as a foreign key for all the controls it contains
class Forms(models.Model):
    name = models.CharField(db_column='name', max_length=255, blank=False, null=False)

    def __str__(self):
        return '%s' % (self.name)

    class Meta:
        managed = True
        db_table = 'tbl_forms'

# This is the actual control that you create with all of its information
class FormBuilder(models.Model):
    form = models.ForeignKey(Forms, on_delete=models.CASCADE, db_column='form', blank=False, null=False, default=1)
    type = models.CharField(db_column='type', max_length=50, blank=False, null=False)
    name = models.CharField(db_column='name', max_length=255, blank=False, null=False)
    label = models.CharField(db_column='label', max_length=255, blank=False, null=False)
    value = models.CharField(db_column='value', max_length=255, blank=True, null=True)
    disabled = models.BooleanField(db_column='disabled', default=False)
    placeholder = models.CharField(db_column='placeholder', max_length=255, blank=True, null=True)
    validation = models.ManyToManyField('FormBuilderExtras', through='FormBuilderExtrasJunction')
    ranking = models.IntegerField(db_column='ranking', blank=True, null=True)

    def __str__(self):
        return '%s %s' % (self.formName, self.name)

    class Meta:
        managed = True
        db_table = 'tbl_formbuilder'

# This may be extra information that you want, like all the validation requirements added like this for in case you have more than one per control
class FormBuilderExtras(models.Model):
    item = models.CharField(db_column='item', max_length=50, blank=False, null=False)
    # Name can be added here as well
    value = models.IntegerField(db_column='value', blank=True, null=True)
    number = models.IntegerField(db_column='number', blank=True, null=True)
    
    def __str__(self):
        return '%s %s' % (self.formBuilder, self.item)

    class Meta:
        managed = True
        db_table = 'tbl_formbuilderextras'

class FormBuilderExtrasJunction(models.Model):
    formBuilderID = models.ForeignKey(FormBuilder, db_column='formBuilderID', on_delete=models.CASCADE) 
    formBuilderExtrasID = models.ForeignKey(FormBuilderExtras, db_column='formBuilderExtrasID', on_delete=models.CASCADE) 
    
    def __str__(self):
        return '%s %s' % (self.formBuilderID, self.formBuilderExtrasID)

    class Meta:
        managed = True
        db_table = 'tbl_formbuilderextrasjunction'