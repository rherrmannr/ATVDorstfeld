from django.contrib.auth.models import User
from django.db import models


class Court(models.Model):
    title = models.CharField(max_length=100)
    used = models.BooleanField(default=False)
    double_field = models.BooleanField(default=True)
    full_hour = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Reservation(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player1", null=True, default=author)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player2", null=True, blank=True)
    player3 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player3", null=True, blank=True)
    player4 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player4", null=True, blank=True)

    def __str__(self):
        return str(self.author) if self.author else ''
