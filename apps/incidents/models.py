from django.db import models
from django.conf import settings

class Incident(models.Model):
    INCIDENT_TYPE_CHOICES = [
        ('theft', 'Theft'),
        ('vandalism', 'Vandalism'),
        ('trespassing', 'Trespassing'),
        ('other', 'Other'),
    ]

    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPE_CHOICES)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    reported_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_incident_type_display()} at {self.location} on {self.date}'
