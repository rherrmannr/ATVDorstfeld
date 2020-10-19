from django.db.models.fields import DateTimeCheckMixin
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from courts.model import Court, Reservation
from django.db import models


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


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = ['court', 'start_datetime']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    class Meta:
        model = Reservation
