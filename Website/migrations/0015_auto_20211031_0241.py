# Generated by Django 3.2.8 on 2021-10-30 23:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0014_auto_20211030_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='time_end',
            field=models.TimeField(default=datetime.datetime(2021, 10, 31, 0, 26, 38, 712748, tzinfo=utc), verbose_name='Час кінця'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='type',
            field=models.CharField(choices=[('lesson', 'Урок'), ('test', 'Тест')], default='lesson', max_length=100, verbose_name='Тип'),
        ),
    ]