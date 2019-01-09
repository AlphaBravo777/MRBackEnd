# Generated by Django 2.0.5 on 2018-12-19 16:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrDatabaseModels', '0032_stocktakingtimes_selectivedelete'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mrAdminOffice', '0010_auto_20181219_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(db_column='message')),
                ('dateCreated', models.DateTimeField(auto_now_add=True, db_column='dateCreated', null=True)),
                ('area', models.ForeignKey(db_column='area', default=1, on_delete=django.db.models.deletion.CASCADE, to='mrAdminOffice.ChecklistAreas')),
                ('importance', models.ForeignKey(db_column='importance', default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='mrAdminOffice.MessageLevels')),
                ('timeStampID', models.ForeignKey(db_column='timeStampID', default=1, on_delete=django.db.models.deletion.CASCADE, to='mrDatabaseModels.TimeStamp')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_checklist',
                'managed': True,
            },
        ),
    ]
