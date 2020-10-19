from django.contrib import admin

from courts.model import Court, Reservation

admin.site.register(Court)
admin.site.register(Reservation)