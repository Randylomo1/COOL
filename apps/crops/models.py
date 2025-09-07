from django.db import models
from django.utils import timezone

class Crop(models.Model):
    name = models.CharField(max_length=100, default='')
    variety = models.CharField(max_length=100, default='')
    planting_date = models.DateField(default=timezone.now)
    estimated_harvest_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
