from django.db import models
from django.utils import timezone

class Finance(models.Model):
    date = models.DateField(default=timezone.now)
    income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    expenses = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return str(self.date)
