from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from apps.customers.models import Customer
from apps.flights.models import Flight

from .models import Booking
from .permissions import AllowPostWithoutAuth
from .serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowPostWithoutAuth]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Booking.objects.filter(
                customer__user=self.request.user
            ).select_related("flight", "customer", "flight__plane")
        return Booking.objects.none()


@login_required
def create_booking(request, flight_id):
    """
    Handle booking creation flow.

    Allows authenticated users to create a booking by:
    - providing passenger data (name and email)
    - selecting a seat number

    Automatically creates or retrieves a Customer linked to the user.
    """
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        seat_number = request.POST.get("seat_number")

        if not seat_number:
            return render(
                request,
                "pages/create_booking.html",
                {
                    "flight": flight,
                    "error": "Informe um número de assento válido",
                },
            )

        seat_number = int(seat_number)

        customer, _ = Customer.objects.get_or_create(
            user=request.user, email=email, defaults={"name": name}
        )

        try:
            Booking.objects.create(
                flight=flight, customer=customer, seat_number=seat_number
            )
            return redirect("flights_list")

        except ValidationError as e:
            error_message = e.message_dict if hasattr(e, "message_dict") else str(e)
            return render(
                request,
                "pages/create_booking.html",
                {
                    "flight": flight,
                    "error": error_message,
                },
            )

    return render(
        request,
        "pages/create_booking.html",
        {"flight": flight},
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(customer__user=request.user).select_related(
        "customer", "flight", "flight__plane"
    )
    return render(request, "pages/my_bookings.html", {"bookings": bookings})


@login_required
def delete_booking(request, booking_id):
    """Delete a booking belonging to the authenticated user."""

    booking = get_object_or_404(Booking, id=booking_id, customer__user=request.user)

    booking.delete()
    return redirect("my_bookings")
