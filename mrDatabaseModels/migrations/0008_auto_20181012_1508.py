# Generated by Django 2.0.5 on 2018-10-12 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0007_auto_20181012_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='unitweight',
            field=models.ForeignKey(blank=True, db_column='unitweight', null=True, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.MeasuringUnits'),
        ),
    ]
