from rest_framework import serializers

from .models import Flight


class FlightSerializer(serializers.ModelSerializer):
    """
    Serializer for Flight model.

    Converts flight data to and from JSON representation,
    including relationships with Plane.
    """

    class Meta:
        model = Flight
        fields = "__all__"
