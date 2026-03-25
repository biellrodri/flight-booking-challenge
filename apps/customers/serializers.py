from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for Customer model.

    Handles serialization and deserialization of customer data,
    including basic validation such as unique email constraint.
    """

    class Meta:
        model = Customer
        fields = "__all__"
