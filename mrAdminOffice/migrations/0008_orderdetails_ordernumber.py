# Generated by Django 2.0.5 on 2019-07-06 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrAdminOffice', '0007_auto_20190531_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='orderNumber',
            field=models.CharField(blank=True, db_column='orderNumber', max_length=40, null=True),
        ),
    ]
