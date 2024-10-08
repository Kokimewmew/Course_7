# Generated by Django 5.1 on 2024-08-22 03:12

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(blank=True, help_text='Действие, которое представляет собой привычка.', max_length=100, null=True, verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='duration',
            field=models.DurationField(blank=True, help_text='Время, которое  потратит пользователь на выполнение привычки.', null=True, validators=[django.core.validators.MaxValueValidator(datetime.timedelta(seconds=120))], verbose_name='Время на выполнение (сек)'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Каждый день'), (2, 'Каждый будний день'), (3, 'Каждые выходные'), (4, 'Каждую неделю')], default=1, help_text='Периодичность выполнения привычки для напоминания в днях.', null=True, verbose_name='Периодичность'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(blank=True, help_text='Место, в котором необходимо выполнять привычку.', max_length=100, null=True, verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(blank=True, help_text='Время, когда необходимо выполнять привычку.', null=True, verbose_name='Время'),
        ),
    ]
