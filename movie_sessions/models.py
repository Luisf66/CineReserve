from django.db import models

# Create your models here.
class Session(models.Model):
    movie = models.ForeignKey(
        'movies.Movie',
        on_delete=models.PROTECT,
        related_name="sessions",
        db_index=True
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    room_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["movie", "room_number", "start_time"],
                name="unique_session_per_room_time"
            )
        ]

    def __str__(self):
        return f"{self.movie} - {self.start_time}"