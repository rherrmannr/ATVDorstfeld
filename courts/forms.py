import datetime

from django.forms import DateTimeField, DurationField, CharField
from django.forms.utils import ErrorList
from django.views.generic import CreateView
from django import forms

from courts.model import Reservation

HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(6, 22)]

MY_CHOICES = [
    (datetime.datetime(year=2020, month=10, day=20, hour=8), '2020-10-20 8:00'),
    (datetime.datetime(year=2020, month=10, day=20, hour=9), '2020-10-20 9:00'),
]

MY_CHOICES2 = [
    (datetime.datetime(year=2020, month=10, day=20, hour=8), '2020-10-20 10:00'),
    (datetime.datetime(year=2020, month=10, day=20, hour=9), '2020-10-20 11:00'),
]


class ReservationCreateView(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court', 'start_datetime']
        widgets = {'start_datetime': forms.Select(choices=MY_CHOICES)}


class CourtSelectionView(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court']


def get_date_time_selection_view_class(court):
    class DatetimeSelectionView(forms.ModelForm):
        class Meta(object):
            print(court)
            model = Reservation
            fields = ['start_datetime']
            if court == 1:
                widgets = {'start_datetime': forms.Select(choices=MY_CHOICES)}
            if court == 2:
                widgets = {'start_datetime': forms.Select(choices=MY_CHOICES2)}

    return DatetimeSelectionView
