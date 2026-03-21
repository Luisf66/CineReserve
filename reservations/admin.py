from django.contrib import admin
from .models import Reservation


# Register your models here.
class ReservationAdmin(admin.ModelAdmin):
    model = Reservation
    list_display = ('user', 'session', 'seat_number', 'status', 'locked_until', 'created_at')

admin.site.register(Reservation, ReservationAdmin)
