# Generated by Django 5.0.2 on 2024-02-20 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_cell_phone_account_work_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='occupation',
        ),
    ]
