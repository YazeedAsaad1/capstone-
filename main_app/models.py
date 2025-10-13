from django.db import models
from django.urls import reverse

class List(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(max_length=250)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.id})