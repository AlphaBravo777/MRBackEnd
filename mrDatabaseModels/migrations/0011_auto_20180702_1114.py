# Generated by Django 2.0.5 on 2018-07-02 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0010_processedstockamounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='processedstockamounts',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.StockTakingTimes'),
        ),
        migrations.AlterField(
            model_name='processedstockamounts',
            name='prodName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist'),
        ),
    ]
