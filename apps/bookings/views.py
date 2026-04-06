from django.contrib.auth.decorators import login_required
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


@login_required
def create_booking(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        seat_number = int(request.POST.get("seat_number"))

        customer, _ = Customer.objects.get_or_create(
            user=request.user, email=email, defaults={"name": name}
        )

        try:
            Booking.objects.create(
                flight=flight, customer=customer, seat_number=seat_number
            )
            return redirect("flights_list")

        except ValidationError as e:
            return render(
                request,
                "pages/create_booking.html",
                {
                    "flight": flight,
                    "error": str(e),
                },
            )

    return render(
        request,
        "pages/create_booking.html",
        {"flight": flight},
    )


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer__user=request.user)

    return render(request, "pages/my_bookings.html", {"bookings": bookings})


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer__user=request.user)

    booking.delete()
    return redirect("my_bookings")
