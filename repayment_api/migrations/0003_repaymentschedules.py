# Generated by Django 4.1.3 on 2022-11-23 09:11

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repayment_api', '0002_alter_loan_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepaymentSchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_no', models.PositiveIntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=6, max_digits=21)),
                ('principal', models.DecimalField(decimal_places=6, max_digits=21)),
                ('interest', models.DecimalField(decimal_places=6, max_digits=21)),
                ('balance', models.DecimalField(decimal_places=6, max_digits=21)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(default=datetime.date(2022, 11, 23))),
                ('date', models.DateField()),
                ('loan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repayment_api.loan')),
            ],
        ),
    ]
