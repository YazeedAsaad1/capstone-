from django.db import models

class List(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(max_length=250)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task
