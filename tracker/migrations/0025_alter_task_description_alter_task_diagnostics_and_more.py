# Generated by Django 5.0.2 on 2024-02-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0024_rename_ticket_history_task_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='diagnostics',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workorder',
            name='subject',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
