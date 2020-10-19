import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Court(models.Model):
    title = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    double_field = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return str(self.author) if self.author else ''

    def get_absolute_url(self):
        return reverse('courts-home')
