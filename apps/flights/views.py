from rest_framework import viewsets
from serializers import FlightSerializer

from .models import Flight


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
