from rest_framework import serializers

from .models import Plane


class PlaneSerializer(serializers.ModelSerializer):
    """
    Serializer for Plane model.

    Responsible for handling aircraft data,
    includin"""

    class Meta:
        model = Plane
        fields = "__all__"
