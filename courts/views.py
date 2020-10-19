import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView

from courts.forms import ReservationCreateView
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
