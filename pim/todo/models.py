from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default = "", blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    complete_date = models.DateTimeField(null=True, blank=True)