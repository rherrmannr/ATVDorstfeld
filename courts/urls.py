from django.urls import path
from . import views as court_view
from .views import CourtsListView

urlpatterns = [
    path('', CourtsListView.as_view(), name='courts-home'),
    path('reservation/new/', court_view.reserve, name='reservation-create'),

]