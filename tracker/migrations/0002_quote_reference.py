# Generated by Django 5.0.2 on 2024-03-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='reference',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
