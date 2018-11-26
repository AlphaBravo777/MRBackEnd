# Generated by Django 2.0.5 on 2018-05-31 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiBucketlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField()),
            ],
            options={
                'db_table': 'api_bucketlist',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblProductlist',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('productid', models.CharField(db_column='productID', max_length=20, unique=True)),
                ('proddescription', models.CharField(blank=True, db_column='prodDescription', max_length=255, null=True)),
                ('packaging', models.IntegerField(blank=True, null=True)),
                ('unitweight', models.FloatField(blank=True, db_column='unitWeight', null=True)),
            ],
            options={
                'db_table': 'tbl_productlist',
                'managed': True,
            },
        ),
    ]
