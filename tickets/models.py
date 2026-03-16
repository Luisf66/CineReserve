from django.db import models

# Create your models here.
class Ticket(models.Model):

    class TicketStatus(models.TextChoices):
        PURCHASED = "purchased", "Purchased"

    user = models.ForeignKey('users.User', on_delete=models.PROTECT)
    session = models.ForeignKey('sessions.Session', on_delete=models.PROTECT)

    seat_number = models.CharField(max_length=4, db_index=True)

    status = models.CharField(
        max_length=10,
        choices=TicketStatus.choices,
        default=TicketStatus.PURCHASED
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["session", "seat_number"],
                name="unique_seat_per_session"
            )
        ]

    def __str__(self):
        return f"{self.session} - {self.seat_number}"