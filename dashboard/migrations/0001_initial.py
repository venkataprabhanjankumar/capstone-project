# Generated by Django 4.1.2 on 2022-10-19 02:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=225)),
                ('description', models.CharField(blank=True, max_length=225)),
                ('access_time', models.DateTimeField(default=datetime.datetime(2022, 10, 19, 8, 23, 31, 61843))),
                ('file', models.FileField(upload_to='personalFiles')),
            ],
        ),
    ]