# Generated by Django 2.0.5 on 2018-09-11 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0030_processedstockamounts_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processedstockamounts',
            old_name='created',
            new_name='dateCreated',
        ),
    ]
