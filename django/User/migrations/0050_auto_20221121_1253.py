# Generated by Django 2.2.8 on 2022-11-21 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0049_auto_20221121_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentmodel',
            name='image',
            field=models.ImageField(default=1, upload_to='images/team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 53, 27, 863672), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 53, 27, 863652), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='12:53:27'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='12:53:27'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 53, 27, 864700), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 21, 12, 53, 27, 864685), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='12:53:27'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='12:53:27'),
        ),
        migrations.AlterField(
            model_name='turfcommentsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 21, 12, 53, 27, 865983), max_length=30),
        ),
    ]
