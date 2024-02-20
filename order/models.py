from django.db import models
from datetime import date
from tracker.models import Task
# Create your models here.
class Quote(models.Model):
    STATUS_CHOICES = (
        ('Pending Approval', 'Pending Approval'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Received', 'Recieved'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,blank=True,  null =True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='quotes/',blank=True,  null =True)
    amountCAD = models.DecimalField(max_digits=10, decimal_places=2)
    date_requested = models.DateField(default=date.today)
    def __str__(self):
        return f"Qoute # {self.id}"