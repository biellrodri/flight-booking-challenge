from django.core.exceptions import ValidationError
from django.db import models


class Booking(models.Model):
    flight = models.ForeignKey(
        "flights.Flight", on_delete=models.CASCADE, related_name="bookings"
    )
    customer = models.ForeignKey(
        "customers.Customer", on_delete=models.CASCADE, related_name="bookings"
    )

    seat_number = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)

    def clean(self):
        """
        Validates booking business rules before saving.

        This method ensures:
        - The flight does not exceed its maximum seat capacity (no overbooking).
        - The seat number is within a valid range (greater than 0 and within plane capacity).
        - The selected seat is not already assigned to another booking in the same flight.

        Notes:
        - Uses `exclude(pk=self.pk)` to avoid counting the current instance
          when updating an existing booking.
        """
        total_seats = self.flight.plane.total_seats
        booked_seats = self.flight.bookings.exclude(pk=self.pk).count()

        errors = {}

        if booked_seats >= total_seats:
            errors["flight"] = (
                "Todos os assentos estão ocupados para este voo. Por favor, selecione outra opção de voo para esse destino."
            )

        if self.seat_number < 1:
            errors["seat_number"] = (
                "O número de assento deve ser maior que 0. Por favor, tente novamente."
            )

        if self.seat_number > total_seats:
            errors["seat_number"] = (
                "Número de assento inválido. Verifique a quantidade máxima de assentos para esta aeronave e tente de novo."
            )

        if (
            self.flight.bookings.filter(seat_number=self.seat_number)
            .exclude(pk=self.pk)
            .exists()
        ):
            errors["seat_number"] = (
                "Este assento já está ocupado. Por favor, verifique os números de assento disponíveis e tente novamente."
            )

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        """
        Override the default save method to enforce validation.

        Calls `full_clean()` to ensure that all field validations,
        model validations, and custom business rules (defined in `clean`)
        are executed before saving the instance to the database.
        """
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer} | Flight {self.flight.id} | Seat {self.seat_number}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["flight", "seat_number"], name="unique_seat_per_flight"
            )
        ]
