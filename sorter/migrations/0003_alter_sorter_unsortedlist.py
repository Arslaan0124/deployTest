# Generated by Django 3.2.6 on 2021-10-30 13:51

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('sorter', '0002_auto_20211030_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sorter',
            name='unsortedList',
            field=models.CharField(default=[], max_length=10, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message=None)]),
        ),
    ]
