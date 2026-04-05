from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from apps.customers.models import Customer
from apps.flights.models import Flight
from apps.planes.models import Plane


class BookingAPITest(APITestCase):

    def setUp(self):
        self.plane = Plane.objects.create(name="Boeing", total_seats=2)

        self.flight = Flight.objects.create(
            origin="SP",
            destination="RJ",
            departure_time=date(2026, 6, 12),
            plane=self.plane,
        )

        self.customer = Customer.objects.create(
            name="Gabriel", email="gabriel@email.com"
        )

    def test_create_booking(self):
        data = {
            "flight": self.flight.pk,
            "customer": self.customer.pk,
            "seat_number": 1,
        }

        response = self.client.post("/api/bookings/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_duplicate_seat(self):
        self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": self.customer.pk, "seat_number": 1},
        )

        response = self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": self.customer.pk, "seat_number": 1},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_overbooking(self):
        customer2 = Customer.objects.create(name="Felipe", email="felipe@email.com")

        self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": self.customer.pk, "seat_number": 1},
        )

        self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": customer2.pk, "seat_number": 2},
        )

        customer3 = Customer.objects.create(name="Julia", email="julia@email.com")

        response = self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": customer3.pk, "seat_number": 1},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalpk_seat(self):
        response = self.client.post(
            "/api/bookings/",
            {"flight": self.flight.pk, "customer": self.customer.pk, "seat_number": 99},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
