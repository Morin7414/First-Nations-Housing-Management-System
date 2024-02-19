# Generated by Django 5.0.2 on 2024-02-18 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_remove_quote_date_approved_remove_quote_worker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_opened',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='quote',
            name='date_requested',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='date_opened',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
