# Generated by Django 2.0.5 on 2019-09-04 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0012_packaging_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlist',
            name='unitsPerMaxShippingWeight',
            field=models.IntegerField(blank=True, db_column='unitsPerMaxShippingWeight', help_text='This is the normal amount of units that can fit into a shipping container, like there are max 10 units SG2 in a red crate', null=True),
        ),
    ]
