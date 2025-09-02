from django.db import models

class Livestock(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    acquisition_date = models.DateField()

    def __str__(self):
        return self.name
