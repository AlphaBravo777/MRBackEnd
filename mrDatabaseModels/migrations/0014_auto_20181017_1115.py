# Generated by Django 2.0.5 on 2018-10-17 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0013_processedstockamounts_prodcontainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factoryarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(db_column='area', max_length=255, unique=True)),
                ('areaRanking', models.IntegerField(db_column='areaRanking', unique=True)),
            ],
            options={
                'db_table': 'tbl_factoryarea',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Factorysubarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subArea', models.CharField(db_column='subArea', max_length=255, unique=True)),
                ('subAreaRanking', models.IntegerField(db_column='subAreaRanking', unique=True)),
                ('area', models.ForeignKey(blank=True, db_column='area', null=True, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Factoryarea')),
            ],
            options={
                'db_table': 'tbl_factorysubarea',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productcontainers',
            name='factoryRanking',
            field=models.IntegerField(blank=True, db_column='factoryranking', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='productcontainers',
            name='factorySubArea',
            field=models.ForeignKey(blank=True, db_column='factorySubArea', null=True, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Factorysubarea'),
        ),
    ]
