# Generated by Django 2.0.5 on 2018-10-25 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0022_auto_20181022_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcontainers',
            name='containernameid',
            field=models.ForeignKey(db_column='containernameid', on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productcontainernames'),
        ),
        migrations.AlterField(
            model_name='productcontainers',
            name='productid',
            field=models.ForeignKey(db_column='productid', on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist'),
        ),
    ]