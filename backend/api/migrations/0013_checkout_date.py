# Generated by Django 4.2.6 on 2023-11-03 21:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_tipout_formula_is_time_based'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
