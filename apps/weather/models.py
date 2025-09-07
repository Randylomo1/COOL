from django.db import models

class Weather(models.Model):
    location = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    description = models.CharField(max_length=255, default='Sunny')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather in {self.location} at {self.timestamp}"