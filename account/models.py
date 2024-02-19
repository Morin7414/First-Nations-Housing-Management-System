from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    OCCUPATION_CHOICES = [
        ('maintenance_worker', 'Maintenance Worker'),
        ('custodian', 'Custodian'),
        ('groundskeeper', 'Groundskeeper'),
        ('janitor', 'Janitor'),
        ('maintenance_technician', 'Maintenance Technician'),
        ('construction_worker', 'Construction Worker'),
        ('hvac_technician', 'HVAC Technician'),
        # Add more choices as needed
    ]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    occupation = models.CharField(max_length=50, choices=OCCUPATION_CHOICES)
    work_phone = models.CharField(max_length=15, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.occupation, self.work_phone, self.cell_phone