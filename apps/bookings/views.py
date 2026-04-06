from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.customers.models import Customer
from apps.flights.models import Flight

from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        customer_id = request.POST.get("customer")
        seat_number = int(request.POST.get("seat_number"))

        customer = Customer.objects.get(id=customer_id)

        try:
            Booking.objects.create(
                flight=flight, customer=customer, seat_number=seat_number
            )
            return redirect("flight_list")

        except ValidationError as e:
            return render(
                request,
                "pages/create_booking.html",
                {
                    "flight": flight,
                    "customers": Customer.objects.all(),
                    "error": str(e),
                },
            )

    return render(
        request,
        "pages/create_booking.html",
        {"flight": flight, "customers": Customer.objects.all()},
    )
