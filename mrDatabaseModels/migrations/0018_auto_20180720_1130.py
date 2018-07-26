# Generated by Django 2.0.5 on 2018-07-20 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0017_auto_20180719_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productgroupnames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(blank=True, db_column='groupName', max_length=255, null=True)),
                ('group', models.CharField(blank=True, max_length=255, null=True)),
                ('grouprating', models.IntegerField(blank=True, db_column='groupRating', null=True)),
            ],
            options={
                'db_table': 'tbl_productgroupnames',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupnameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productgroupnames')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist')),
            ],
            options={
                'db_table': 'tbl_productgroups',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productgroupnames',
            name='members',
            field=models.ManyToManyField(through='mrDatabaseModels.Productgroups', to='mrDatabaseModels.Productlist'),
        ),
    ]