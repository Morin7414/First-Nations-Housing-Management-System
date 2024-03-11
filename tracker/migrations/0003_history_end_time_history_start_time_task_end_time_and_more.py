# Generated by Django 5.0.2 on 2024-03-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_quote_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Pending Parts', 'Pending Parts'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20, null=True),
        ),
    ]
