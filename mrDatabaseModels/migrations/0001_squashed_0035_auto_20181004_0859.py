# Generated by Django 2.0.5 on 2018-10-04 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('mrDatabaseModels', '0001_initial'), ('mrDatabaseModels', '0002_packaging_tbldeliveryroutes'), ('mrDatabaseModels', '0003_remove_productlist_packaging'), ('mrDatabaseModels', '0004_productlist_packaging'), ('mrDatabaseModels', '0005_productbrands'), ('mrDatabaseModels', '0006_productlist_brand'), ('mrDatabaseModels', '0007_stocktakingtimes'), ('mrDatabaseModels', '0008_delete_stocktakingtimes'), ('mrDatabaseModels', '0009_stocktakingtimes'), ('mrDatabaseModels', '0010_processedstockamounts'), ('mrDatabaseModels', '0011_auto_20180702_1114'), ('mrDatabaseModels', '0012_auto_20180703_0826'), ('mrDatabaseModels', '0013_auto_20180706_1043'), ('mrDatabaseModels', '0014_auto_20180709_0942'), ('mrDatabaseModels', '0015_auto_20180709_1002'), ('mrDatabaseModels', '0016_auto_20180709_1202'), ('mrDatabaseModels', '0017_auto_20180719_0912'), ('mrDatabaseModels', '0018_auto_20180720_1130'), ('mrDatabaseModels', '0019_auto_20180720_1214'), ('mrDatabaseModels', '0020_auto_20180720_1229'), ('mrDatabaseModels', '0021_prosstock'), ('mrDatabaseModels', '0022_auto_20180720_1522'), ('mrDatabaseModels', '0023_auto_20180723_1417'), ('mrDatabaseModels', '0024_productlist_stocktakegroup'), ('mrDatabaseModels', '0025_productcontainers_deletecontaineramount'), ('mrDatabaseModels', '0026_auto_20180830_0726'), ('mrDatabaseModels', '0027_highriskpackinglist'), ('mrDatabaseModels', '0028_auto_20180910_0847'), ('mrDatabaseModels', '0029_auto_20180911_0942'), ('mrDatabaseModels', '0030_processedstockamounts_created'), ('mrDatabaseModels', '0031_auto_20180911_1356'), ('mrDatabaseModels', '0032_batchgroups_packinglistranking'), ('mrDatabaseModels', '0033_productlist_packlistgroup'), ('mrDatabaseModels', '0034_auto_20181003_2042'), ('mrDatabaseModels', '0035_auto_20181004_0859')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batchgroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchname', models.CharField(db_column='batchName', max_length=255, unique=True)),
                ('ranking', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'tbl_batchgroups',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(db_column='productID', max_length=20, unique=True)),
                ('proddescription', models.CharField(blank=True, db_column='prodDescription', max_length=255, null=True)),
                ('unitweight', models.FloatField(blank=True, db_column='unitWeight', null=True)),
                ('packageweight', models.FloatField(blank=True, db_column='packageWeight', null=True)),
                ('productonhold', models.IntegerField(blank=True, db_column='productOnHold', null=True)),
                ('batchranking', models.IntegerField(blank=True, db_column='batchRanking', null=True)),
                ('batchgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Batchgroups')),
            ],
            options={
                'db_table': 'tbl_productlist',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packaging_type', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_packaging',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TblDeliveryroutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routes', models.CharField(max_length=255, unique=True)),
                ('loadingday', models.IntegerField(blank=True, db_column='loadingDay', null=True)),
            ],
            options={
                'db_table': 'tbl_deliveryroutes',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productlist',
            name='packaging',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Packaging'),
        ),
        migrations.CreateModel(
            name='ProductBrands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_productbrands',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productlist',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.ProductBrands'),
        ),
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
        migrations.CreateModel(
            name='ProcessedStockAmounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=255)),
                ('prodName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist')),
                ('time', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.StockTakingTimes')),
            ],
            options={
                'db_table': 'tbl_processedStockAmounts',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='productlist',
            name='productid',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='productlist',
            name='productonhold',
            field=models.BooleanField(default=False),
        ),
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
        migrations.CreateModel(
            name='Productcontainernames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('containername', models.CharField(blank=True, db_column='groupName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tbl_productcontainernames',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productcontainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('containernameid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productcontainernames')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist')),
                ('deleteContainerAmount', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_productcontainers',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='productcontainernames',
            name='members',
            field=models.ManyToManyField(through='mrDatabaseModels.Productcontainers', to='mrDatabaseModels.Productlist'),
        ),
        migrations.AlterField(
            model_name='productcontainernames',
            name='containername',
            field=models.CharField(blank=True, db_column='containerName', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='processedstockamounts',
            name='container',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productcontainernames'),
        ),
        migrations.AddField(
            model_name='productlist',
            name='stocktakegroup',
            field=models.ForeignKey(db_column='stocktakegroup', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='stocktakegroup', to='mrDatabaseModels.Batchgroups'),
        ),
        migrations.AlterModelOptions(
            name='productlist',
            options={'managed': True, 'ordering': ['productid']},
        ),
        migrations.AlterField(
            model_name='stocktakingtimes',
            name='times',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='HighRiskPackingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentStock', models.IntegerField(db_column='currentStock')),
                ('stockNeeded', models.IntegerField(db_column='stockNeeded')),
                ('productCode', models.OneToOneField(db_column='productCode', on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist')),
            ],
            options={
                'db_table': 'tbl_highRiskPackingList',
                'managed': True,
                'ordering': ['productCode'],
            },
        ),
        migrations.AddField(
            model_name='processedstockamounts',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='batchgroups',
            name='packingListRanking',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='productlist',
            name='packlistgroup',
            field=models.ForeignKey(db_column='packlistgroup', default=20, on_delete=django.db.models.deletion.CASCADE, related_name='packlistgroup', to='mrDatabaseModels.Batchgroups'),
        ),
        migrations.AlterModelTable(
            name='highriskpackinglist',
            table='tbl_highriskpackingList',
        ),
        migrations.AlterModelTable(
            name='processedstockamounts',
            table='tbl_processedstockamounts',
        ),
        migrations.AlterModelTable(
            name='stocktakingtimes',
            table='tbl_stocktakingtimes',
        ),
        migrations.AlterField(
            model_name='processedstockamounts',
            name='container',
            field=models.ForeignKey(db_column='container', default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productcontainernames'),
        ),
        migrations.AlterField(
            model_name='processedstockamounts',
            name='prodName',
            field=models.ForeignKey(db_column='prodName', on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.Productlist'),
        ),
        migrations.AlterField(
            model_name='processedstockamounts',
            name='time',
            field=models.ForeignKey(db_column='time', default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.StockTakingTimes'),
        ),
    ]