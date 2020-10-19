import datetime

from django.forms import DateTimeField, DurationField
from django.views.generic import CreateView
from django import forms

from courts.model import Reservation

HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(6, 22)]

MY_CHOICES = [
    (datetime.datetime(year=2020, month=10, day=20, hour=8), '2020-10-20 8:00'),
    (datetime.datetime(year=2020, month=10, day=20, hour=9), '2020-10-20 9:00'),
]


class ReservationCreateView(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court', 'start_datetime']
        widgets = {'start_datetime': forms.Select(choices=MY_CHOICES)}
