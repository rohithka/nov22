# Generated by Django 2.2.8 on 2022-11-21 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0045_auto_20221121_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 22, 10, 477400), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 22, 10, 477380), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='12:22:10'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='12:22:10'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 22, 10, 478391), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 22, 10, 478376), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='team_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='12:22:10'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='12:22:10'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='team_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='turfcommentsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 12, 22, 10, 479668), max_length=30),
        ),
    ]