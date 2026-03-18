from django.core.exceptions import ValidationError
from django.db import models


class Booking(models.Model):
    flight = models.ForeignKey(
        "flights.Flight", on_delete=models.CASCADE, related_name="bookings"
    )
    customer = models.ForeignKey(
        "customer.Customer", on_delete=models.CASCADE, related_name="bookings"
    )

    seat_number = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def clean(self):
        total_seats = self.flight.plane.total_seats
        booked_seats = self.flight.bookings.count()

        if booked_seats >= total_seats:
            raise ValidationError("Todos os assentos ocupados para este voo.")

        if self.seat_number > total_seats:
            raise ValidationError("Número de assento inválido")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer} - {self.flight}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["flight", "seat_number"], name="unique_seat_per_flight"
            )
        ]
