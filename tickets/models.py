from django.db import models


class Ticket(models.Model):

    reservation = models.OneToOneField(
        'reservations.Reservation',
        on_delete=models.PROTECT,
        related_name='ticket'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reservation.session} - {self.reservation.seat_number}"