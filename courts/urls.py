from django.urls import path
from . import views
from .views import CourtsListView

urlpatterns = [
    path('', CourtsListView.as_view(), name='courts-home'),
]