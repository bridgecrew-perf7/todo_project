from django.db import models
from django.utils import timezone


# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
        ('IP', 'IN_PROGRESS'),
        ('D', 'DROPPED'),
    )

    status = models.CharField(choices=STATUS_CHOICES, max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.content}-{self.task_list}"
