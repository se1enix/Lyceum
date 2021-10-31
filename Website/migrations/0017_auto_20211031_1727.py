# Generated by Django 3.2.8 on 2021-10-31 15:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0016_auto_20211031_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='phone',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time_end',
            field=models.TimeField(default=datetime.datetime(2021, 10, 31, 16, 12, 18, 804406, tzinfo=utc), verbose_name='Час кінця'),
        ),
    ]
