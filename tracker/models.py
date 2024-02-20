from django.db import models
from django.contrib.auth.models import User, Group
from datetime import date
from community_units.models import CommunityEntity

class WorkOrder(models.Model):
    STATUS_CHOICES = (
        ('New/Open', 'New/Open'),
        ('In Progress', 'In Progress'),
        ('Pending Review', 'Pending Review'),
        ('On Hold', 'On Hold'),
        ('Resolved/Closed', 'Resolved/Closed'),
        ('Cancelled', 'Cancelled'),
        ('Reopened', 'Reopened'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    house = models.ForeignKey(CommunityEntity,on_delete=models.CASCADE, null=True,blank=True,)
    coordinator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_opened = models.DateField(default=date.today)
    date_closed = models.DateField(blank=True,  null =True)

   # image = models.ImageField(upload_to='images/',blank=True,  null =True)
   # description = models.TextField(blank=True, null=True)
    subject = models.TextField(max_length=255,)

    
    def __str__(self):
        return f"Work Order # {self.id}"


class Task(models.Model):
    STATUS_CHOICES = (
        ('New/Open', 'New/Open'),
        ('In Progress', 'In Progress'),
        ('Pending Approval', 'Pending Approval'),
        ('Pending Parts', 'Pending Parts'),
        ('Resolved/Closed', 'Resolved/Closed'),
        ('Cancelled', 'Cancelled'),
        ('Reopened', 'Reopened'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    work_order = models.ForeignKey('WorkOrder', on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True,  null =True)
    description = models.TextField(max_length=255,)
    assigned_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    assigned_worker =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_opened = models.DateField(default=date.today)
    date_completed = models.DateField(blank=True,  null =True)
    diagnostics = models.TextField(max_length=255,)

    def __str__(self):
        return f"Task # {self.id}"
    


class History(models.Model):
    status = models.CharField(max_length=20,blank=True,  null =True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL,blank=True, null=True)
    image = models.ImageField(blank=True,  null =True)
    assigned_worker =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    diagnostics = models.TextField(max_length=255,blank=True, null=True)
    date = models.DateField(blank=True,  null =True)

    def __str__(self):
        return f"{self.date}"
    





