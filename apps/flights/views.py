from django.shortcuts import render
from rest_framework import viewsets

from .models import Flight
from .serializers import FlightSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


def flights_list(request):
    flights = Flight.objects.all().order_by("departure_time")

    return render(request, "pages/flights.html", {"flights": flights})
