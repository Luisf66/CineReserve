from django.db import models


class Reservation(models.Model):

    class ReservationStatus(models.TextChoices):
        LOCKED = "locked", "Locked"
        EXPIRED = "expired", "Expired"

    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    session = models.ForeignKey('sessions.Session', on_delete=models.PROTECT)

    seat_number = models.CharField(max_length=3, db_index=True)

    status = models.CharField(
        max_length=10,
        choices=ReservationStatus.choices,
        default=ReservationStatus.LOCKED
    )

    locked_until = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)