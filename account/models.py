from django.db import models
from django.contrib.auth.models import User, Group


# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    work_phone = models.CharField(max_length=15, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
