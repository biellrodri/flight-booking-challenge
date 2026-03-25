from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    """

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.message_dict)

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.message_dict)

    class Meta:
        model = Booking
        fields = "__all__"
        validators = []
