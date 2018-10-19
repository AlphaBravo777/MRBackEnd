# Generated by Django 2.0.5 on 2018-10-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0006_measuringunits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colorcodes',
            name='colorCode',
            field=models.CharField(db_column='colorCode', max_length=10),
        ),
        migrations.AlterField(
            model_name='colorcodes',
            name='itemDescription',
            field=models.CharField(db_column='itemDescription', max_length=100),
        ),
        migrations.AlterField(
            model_name='measuringunits',
            name='measuringUnit',
            field=models.CharField(db_column='measuringUnit', max_length=100),
        ),
        migrations.AlterField(
            model_name='measuringunits',
            name='unitDescription',
            field=models.CharField(db_column='unitDescription', max_length=100),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='unitweight',
            field=models.ForeignKey(db_column='unitweight', default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.MeasuringUnits'),
        ),
    ]