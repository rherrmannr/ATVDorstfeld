# Generated by Django 3.1.2 on 2020-10-19 16:03

import test
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0007_court_double_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='start_datetime',
            field=models.TimeField(default=test.time(0, 0)),
        ),
    ]
