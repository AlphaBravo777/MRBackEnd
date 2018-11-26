# Generated by Django 2.0.5 on 2018-07-20 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0020_auto_20180720_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProsStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255)),
                ('prodNameContainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productcontainers')),
                ('time', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.StockTakingTimes')),
            ],
            options={
                'db_table': 'tbl_ProsStock',
                'managed': True,
            },
        ),
    ]
