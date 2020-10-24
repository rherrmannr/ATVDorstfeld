from datetime import datetime, timedelta

from django import forms
from django.forms import ModelForm

from courts.model import Reservation, Court


def get_all_choices(future_days=14):
    current = datetime.now()
    all_choices = [
        (datetime(year=current.year, month=current.month, day=current.day, hour=x),
         '{}-{}-{} {:02d}:00'.format(current.year, current.month, current.day, x)) for x in
        range(current.hour + 1, 22)
    ]

    for x in range(1, future_days):
        current = current + timedelta(days=1)
        all_choices.extend([
            (datetime(year=current.year, month=current.month, day=current.day, hour=x),
             '{}-{}-{} {:02d}:00'.format(current.year, current.month, current.day, x)) for x in
            range(6, 21)
        ])
    return all_choices


class ReservationCreateView(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court', 'start_datetime']
        choices = get_all_choices()
        widgets = {'start_datetime': forms.Select(choices=choices)}


class CourtSelectionView(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['court']


def get_available_times_for_court(court_id, days_in_future=14):
    all_choices = get_all_choices(days_in_future)
    reservations = Reservation.objects.filter(court_id=court_id)
    remove_list = []
    for r in reservations:
        year = r.start_datetime.year
        month = r.start_datetime.month
        day = r.start_datetime.day
        hour = r.start_datetime.hour
        remove_list.extend([
            (datetime(year=year, month=month, day=day, hour=r.start_datetime.hour),
             '{}-{}-{} {:02d}:00'.format(year, month, day, hour))
        ])
    return filter(lambda i: i not in remove_list, all_choices)


def get_date_time_selection_view_class(court):
    class DatetimeSelectionView(ModelForm):
        class Meta:
            fields = ['start_datetime', 'player1', 'player2']
            if Court.objects.get(pk=court).double_field:
                fields.extend(["player3", "player4"])
            fields.extend(["contact_details"])
            model = Reservation
            choices = get_available_times_for_court(court)
            widgets = {'start_datetime': forms.Select(choices=choices)}

    return DatetimeSelectionView
