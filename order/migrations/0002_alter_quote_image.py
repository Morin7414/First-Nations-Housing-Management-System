# Generated by Django 5.0.2 on 2024-02-19 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='quotes/'),
        ),
    ]