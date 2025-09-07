from django.db import models
from django.utils import timezone

class Livestock(models.Model):
    name = models.CharField(max_length=100, default='')
    species = models.CharField(max_length=100, default='')
    breed = models.CharField(max_length=100, default='')
    birth_date = models.DateField(default=timezone.now)
    acquisition_date = models.DateField(default=timezone.now)
    health_status = models.CharField(max_length=100, default='Healthy')

    def __str__(self):
        return self.name
