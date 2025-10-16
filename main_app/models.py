from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class List(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField(max_length=2500)
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('detail', kwargs={'item_id': self.id})