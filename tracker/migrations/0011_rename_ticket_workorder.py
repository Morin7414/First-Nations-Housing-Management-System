# Generated by Django 5.0.2 on 2024-02-18 16:18

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('tracker', '0010_alter_ticket_house'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ticket',
            new_name='WorkOrder',
        ),
    ]