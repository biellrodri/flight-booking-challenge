from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.bookings.models import Booking
from apps.customers.models import Customer
from apps.flights.models import Flight
from apps.planes.models import Plane


class BookingModelTest(TestCase):

    def setUp(self):
        self.plane = Plane.objects.create(name="Boeing 737", total_seats=2)

        self.flight = Flight.objects.create(
            origin="SP",
            destination="RJ",
            departure_time=date(2026, 7, 30),
            plane=self.plane,
        )

        self.customer = Customer.objects.create(name="Miguel", email="miguel@gmail.com")

    def test_valid_booking(self):
        booking = Booking(flight=self.flight, customer=self.customer, seat_number=1)

        booking.save()

        self.assertEqual(Booking.objects.count(), 1)

    def test_overbooking(self):
        Booking.objects.create(
            flight=self.flight, customer=self.customer, seat_number=1
        )

        customer2 = Customer.objects.create(name="Gabriel", email="gabriel@gmail.com")

        Booking.objects.create(flight=self.flight, customer=customer2, seat_number=2)

        customer3 = Customer.objects.create(name="João", email="joao@gmail.com")

        booking = Booking(flight=self.flight, customer=customer3, seat_number=1)

        with self.assertRaises(ValidationError):
            booking.save()

    def test_duplicate_seat(self):
        Booking.objects.create(
            flight=self.flight, customer=self.customer, seat_number=2
        )

        customer2 = Customer.objects.create(name="Luana", email="luana@gmail.com")

        booking = Booking(flight=self.flight, customer=customer2, seat_number=2)

        with self.assertRaises(ValidationError):
            booking.save()

    def test_invalid_seat_number(self):
        booking = Booking(flight=self.flight, customer=self.customer, seat_number=99)

        with self.assertRaises(ValidationError):
            booking.save()

    def test_seat_number_less_than_one(self):
        booking = Booking(flight=self.flight, customer=self.customer, seat_number=0)

        with self.assertRaises(ValidationError):
            booking.save()
