# Generated by Django 2.0.5 on 2019-02-25 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrAdminOffice', '0003_orderdetails_accountsid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetails',
            name='routeid',
        ),
    ]