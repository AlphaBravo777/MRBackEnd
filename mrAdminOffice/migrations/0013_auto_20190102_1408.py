# Generated by Django 2.0.5 on 2019-01-02 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrAdminOffice', '0012_dailyreport_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountchild',
            name='mainAccount',
        ),
        migrations.RemoveField(
            model_name='accountgrandchild',
            name='childAccount',
        ),
        migrations.RemoveField(
            model_name='accountgrandchild',
            name='productGroup',
        ),
        migrations.RemoveField(
            model_name='accountgrandchild',
            name='route',
        ),
        migrations.DeleteModel(
            name='AccountChild',
        ),
        migrations.DeleteModel(
            name='AccountGrandChild',
        ),
        migrations.DeleteModel(
            name='AccountName',
        ),
    ]
