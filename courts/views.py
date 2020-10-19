from django.shortcuts import render
from django.views.generic import ListView

from courts.model import Court, Reservation


class CourtsListView(ListView):
    model = Court
    # model = Post -> wird zu court
    template_name = 'courts/home.html'
    context_object_name = 'courts'

    def get_context_data(self, **kwargs):
        context = super(CourtsListView, self).get_context_data(**kwargs)
        context.update({
            'courts': Court.objects.all(),
            'reservations': Reservation.objects.all(),
        })
        return context
