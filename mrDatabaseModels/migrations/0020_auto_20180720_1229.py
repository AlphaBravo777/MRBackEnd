# Generated by Django 2.0.5 on 2018-07-20 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0019_auto_20180720_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontainernames',
            name='containername',
            field=models.CharField(blank=True, db_column='containerName', max_length=255, null=True),
        ),
    ]