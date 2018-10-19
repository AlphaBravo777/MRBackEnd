# Generated by Django 2.0.5 on 2018-10-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0001_squashed_0035_auto_20181004_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='processedstockamounts',
            name='shift',
            field=models.CharField(db_column='shift', default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='processedstockamounts',
            name='week',
            field=models.IntegerField(db_column='week', default=1),
        ),
        migrations.AddField(
            model_name='processedstockamounts',
            name='weekDay',
            field=models.IntegerField(db_column='weekDay', default=1),
        ),
        migrations.AddField(
            model_name='processedstockamounts',
            name='year',
            field=models.IntegerField(db_column='year', default=2018),
        ),
    ]