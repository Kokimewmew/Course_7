# Generated by Django 5.1 on 2024-08-20 16:06

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(help_text='Место, в котором необходимо выполнять привычку.', max_length=100, verbose_name='Место')),
                ('time', models.TimeField(help_text='Время, когда необходимо выполнять привычку.', verbose_name='Время')),
                ('action', models.CharField(help_text='Действие, которое представляет собой привычка.', max_length=100, verbose_name='Действие')),
                ('pleasant_habit', models.BooleanField(default=False, help_text='Привычка, которую можно привязать к выполнению полезной привычки.', verbose_name='Признак приятной привычки')),
                ('periodicity', models.PositiveIntegerField(choices=[(1, 'Каждый день'), (2, 'Каждый будний день'), (3, 'Каждые выходные'), (4, 'Каждую неделю')], default=1, help_text='Периодичность выполнения привычки для напоминания в днях.', verbose_name='Периодичность')),
                ('award', models.CharField(blank=True, help_text='Чем пользователь должен себя вознаградить после выполнения.', max_length=100, null=True, verbose_name='Вознаграждение ')),
                ('duration', models.DurationField(help_text='Время, которое  потратит пользователь на выполнение привычки.', validators=[django.core.validators.MaxValueValidator(datetime.timedelta(seconds=120))], verbose_name='Время на выполнение (сек)')),
                ('is_public', models.BooleanField(default=False, help_text='Другие пользователи могли брать в пример чужие привычки.', verbose_name='Признак публичности')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Создатель привычки')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habit.habit')),
            ],
        ),
    ]
