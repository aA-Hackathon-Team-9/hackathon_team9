# Generated by Django 4.2.6 on 2023-10-25 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('restaurant_employee_id', models.CharField(max_length=10, null=True)),
                ('food_permit_exp', models.DateField(null=True)),
                ('alcohol_permit_exp', models.DateField(null=True)),
                ('is_former_employee', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tipout_Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula_name', models.CharField(max_length=50)),
                ('formula', models.CharField(max_length=255)),
                ('is_am_formula', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Tipout_Variable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable', models.CharField(max_length=255)),
                ('table_name', models.CharField(max_length=255)),
                ('column_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('tipout_formula_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipout_formula')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.employee')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.role')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Clock_In',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_in', models.DateTimeField(null=True)),
                ('time_out', models.DateTimeField(null=True)),
                ('tipout_received', models.DecimalField(decimal_places=2, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('active_role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.role')),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_sales', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cash_owed', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total_tipout', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_am_shift', models.BooleanField(default=True)),
                ('is_patio', models.BooleanField(default=False)),
                ('is_bar', models.BooleanField(default=False)),
                ('tipout_day', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet_cell', models.CharField(default=None, max_length=10, null=True)),
                ('is_uploaded', models.BooleanField(default=False)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.employee')),
            ],
        ),
    ]