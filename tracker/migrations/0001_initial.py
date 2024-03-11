# Generated by Django 5.0.2 on 2024-03-10 23:03

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('community_units', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('New/Open', 'New/Open'), ('In Progress', 'In Progress'), ('Pending Approval', 'Pending Approval'), ('Pending Parts', 'Pending Parts'), ('Resolved/Closed', 'Resolved/Closed'), ('Cancelled', 'Cancelled'), ('Reopened', 'Reopened')], max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(max_length=255)),
                ('date_opened', models.DateField(default=datetime.date.today)),
                ('date_completed', models.DateField(blank=True, null=True)),
                ('diagnostics', models.TextField(max_length=255)),
                ('assigned_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group')),
                ('assigned_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('diagnostics', models.TextField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('assigned_worker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.task')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('New/Open', 'New/Open'), ('In Progress', 'In Progress'), ('Pending Review', 'Pending Review'), ('On Hold', 'On Hold'), ('Resolved/Closed', 'Resolved/Closed'), ('Cancelled', 'Cancelled'), ('Reopened', 'Reopened')], max_length=20, null=True)),
                ('date_opened', models.DateField(default=datetime.date.today)),
                ('date_closed', models.DateField(blank=True, null=True)),
                ('subject', models.TextField(max_length=255)),
                ('Tasks', models.CharField(blank=True, max_length=20, null=True)),
                ('Quotes_Invoices', models.CharField(blank=True, max_length=20, null=True)),
                ('coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('house', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community_units.communityentity')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='work_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.workorder'),
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('status', models.CharField(blank=True, choices=[('Pending Approval', 'Pending Approval'), ('Approved', 'Approved'), ('Declined', 'Declined')], max_length=20, null=True)),
                ('quote', models.FileField(blank=True, null=True, upload_to='housequotes/')),
                ('invoice', models.FileField(blank=True, null=True, upload_to='houseinvoice/')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_requested', models.DateField(default=datetime.date.today)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.company')),
                ('workorder', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracker.workorder')),
            ],
        ),
    ]
