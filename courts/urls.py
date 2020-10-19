from django.urls import path
from . import views as court_view
from .views import CourtsListView

urlpatterns = [
    path('', CourtsListView.as_view(), name='courts-home'),
    path('reservation/select_court/', court_view.select_court, name='select-court'),
    path('reservation/select_datetime/', court_view.select_datetime, name='select-datetime'),
    path('reservation/new/', court_view.reserve, name='reservation-create'),

]