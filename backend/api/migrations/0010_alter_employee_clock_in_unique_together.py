# Generated by Django 4.2.6 on 2023-11-01 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_employee_clock_in_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='employee_clock_in',
            unique_together=set(),
        ),
    ]