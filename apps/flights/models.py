from django.db import models


class Flight(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateField()

    plane = models.ForeignKey(
        "planes.Plane", on_delete=models.CASCADE, related_name="flights"
    )

    def __str__(self):
        return f"{self.origin} -> {self.destination}"
