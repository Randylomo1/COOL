from django.db import models

class Yield(models.Model):
    crop = models.ForeignKey('crops.Crop', on_delete=models.CASCADE, null=True, blank=True)
    livestock = models.ForeignKey('livestock.Livestock', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.FloatField()
    date = models.DateField()

    def __str__(self):
        if self.crop:
            return f'{self.crop.name} - {self.date}'
        elif self.livestock:
            return f'{self.livestock.name} - {self.date}'
        return f'Yield - {self.date}'
