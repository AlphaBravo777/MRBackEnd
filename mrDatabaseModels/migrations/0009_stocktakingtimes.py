# Generated by Django 2.0.5 on 2018-07-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0008_delete_stocktakingtimes'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTakingTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.TimeField(blank=True, unique=True)),
            ],
            options={
                'db_table': 'tbl_stockTakingTimes',
                'managed': True,
            },
        ),
    ]
