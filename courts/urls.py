from django.urls import path
from . import views
from .views import CourtsListView, ReservationCreateView

urlpatterns = [
    path('', CourtsListView.as_view(), name='courts-home'),
    path('reservation/new/', ReservationCreateView.as_view(), name='reservation-create'),

]
