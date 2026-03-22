from rest_framework import serializers

from .models import Plane


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"
