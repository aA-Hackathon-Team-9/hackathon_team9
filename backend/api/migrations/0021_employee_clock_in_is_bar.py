# Generated by Django 4.2.6 on 2023-11-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_checkout_total_owed'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_clock_in',
            name='is_bar',
            field=models.BooleanField(default=False),
        ),
    ]
