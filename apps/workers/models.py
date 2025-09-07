from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
