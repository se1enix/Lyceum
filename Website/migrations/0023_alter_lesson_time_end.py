# Generated by Django 3.2.8 on 2021-11-01 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0022_alter_lesson_time_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='time_end',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Час кінця'),
        ),
    ]