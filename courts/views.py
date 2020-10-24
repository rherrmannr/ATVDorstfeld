import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DeleteView

from courts.forms import ReservationCreateView, CourtSelectionView, get_date_time_selection_view_class
from courts.model import Court, Reservation


class CourtsListView(ListView):
    model = Court
    template_name = 'courts/home.html'
    context_object_name = 'courts'

    def get_context_data(self, **kwargs):
        context = super(CourtsListView, self).get_context_data(**kwargs)
        context.update({
            'courts': Court.objects.all(),
            'reservations': Reservation.objects.all(),
        })
        return context


class ReservationsListView(ListView):
    model = Reservation
    template_name = "courts/reservations.html"
    context_object_name = 'reservations'


class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author


def select_court(request):
    form = CourtSelectionView(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            request.session['temp_data'] = form.instance.court_id
            return redirect('select-datetime')
    return render(request, 'courts/select_court.html', {'form': form})


def select_datetime(request):
    datetime_selection_view_class = get_date_time_selection_view_class(court=request.session['temp_data'])
    form = datetime_selection_view_class(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            if is_using_guest(form) and not has_added_contact_details(form):
                messages.warning(request, f'Bitte die Kontaktdaten für den Gastspieler angeben!')
                return render(request, 'courts/reservation_form.html', {'form': form})
            form.instance.court_id = request.session['temp_data']
            form.instance.author = request.user
            form.instance.end_datetime = form.instance.start_datetime + datetime.timedelta(hours=1)

            messages.success(request, f'Buchung wurde angelegt. Viel Spaß beim Spielen!')
            form.save()
            return redirect('courts-home')
    return render(request, 'courts/reservation_form.html', {'form': form})


def is_using_guest(form):
    using_guest = False
    guest_player = "Gastspieler"
    if hasattr(form.instance.player1, 'username'):
        if form.instance.player1.username == guest_player:
            using_guest = True
    if hasattr(form.instance.player2, 'username'):
        if form.instance.player2.username == guest_player:
            using_guest = True
    if hasattr(form.instance.player3, 'username'):
        if form.instance.player3.username == guest_player:
            using_guest = True
    if hasattr(form.instance.player4, 'username'):
        if form.instance.player4.username == guest_player:
            using_guest = True
    return using_guest


def has_added_contact_details(form):
    return form.instance.contact_details


def reserve(request):
    form = ReservationCreateView(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.author = request.user
            form.instance.end_datetime = form.instance.start_datetime + datetime.timedelta(hours=1)
            messages.success(request, f'Buchung wurde angelegt. Viel Spaß beim Spielen!')
            form.save()
            return redirect('courts-home')
    return render(request, 'courts/reservation_form.html', {'form': form})
