# Generated by Django 5.0.2 on 2024-02-17 18:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('occupation', models.CharField(choices=[('maintenance_worker', 'Maintenance Worker'), ('custodian', 'Custodian'), ('groundskeeper', 'Groundskeeper'), ('janitor', 'Janitor'), ('maintenance_technician', 'Maintenance Technician'), ('construction_worker', 'Construction Worker'), ('hvac_technician', 'HVAC Technician')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
