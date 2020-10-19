from django.db import models
from django.contrib.auth.models import User


class Court(models.Model):
    title = models.CharField(max_length=100)
    used = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.author
