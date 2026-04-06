from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Flight
from .serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related("plane").all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


def flights_list(request):
    """
    Display available flights ordered by departure time.
    """

    flights = Flight.objects.select_related("plane").all().order_by("departure_time")
    return render(request, "pages/flights.html", {"flights": flights})
