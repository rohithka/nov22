# Generated by Django 2.2.8 on 2022-11-17 10:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0026_auto_20221117_1112'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateTeamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 16, 26, 45, 682734), max_length=30),
        ),
        migrations.AlterField(
            model_name='matchmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 16, 26, 45, 682707), max_length=30),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='16:26:45'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='16:26:45'),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='end_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 16, 26, 45, 683661), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='start_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 16, 26, 45, 683648), max_length=30),
        ),
        migrations.AlterField(
            model_name='tournamentmodel',
            name='team_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.CreateTeamModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='end_time',
            field=models.TimeField(blank=True, default='16:26:45'),
        ),
        migrations.AlterField(
            model_name='tournamentrequestmodel',
            name='start_time',
            field=models.TimeField(blank=True, default='16:26:45'),
        ),
        migrations.AlterField(
            model_name='turfcommentsmodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 17, 16, 26, 45, 684864), max_length=30),
        ),
    ]
