# Generated by Django 4.2.6 on 2023-10-26 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_employeerole_employee_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(related_name='employees', through='api.Employee_Role', to='api.role'),
        ),
    ]
