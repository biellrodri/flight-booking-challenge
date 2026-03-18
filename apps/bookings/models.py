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

    def __str__(self):
        return f"{self.customer} - {self.flight}"
