from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate(self, attrs):

        instance = self.instance or Booking(**attrs)

        for field, value in attrs.items():
            setattr(instance, field, value)

        try:

            instance.full_clean()
        except DjangoValidationError as e:

            raise serializers.ValidationError(e.message_dict)

        return attrs
