# Generated by Django 2.0.5 on 2019-07-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrAdminOffice', '0008_orderdetails_ordernumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='accountAccessDBid',
            field=models.IntegerField(db_column='accountAccessDBid', null=True, unique=True),
        ),
    ]
