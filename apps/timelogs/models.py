from django.db import models
from apps.tasks.models import Task
from apps.workers.models import Worker

class TimeLog(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.worker.name} - {self.task.name}'
