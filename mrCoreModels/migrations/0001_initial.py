# Generated by Django 2.0.5 on 2018-11-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SettingsDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value1', models.CharField(db_column='value1', max_length=255)),
            ],
            options={
                'db_table': 'tbl_settingsdb',
                'managed': True,
            },
        ),
    ]
