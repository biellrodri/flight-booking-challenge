from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.bookings.views import BookingViewSet, create_booking
from apps.customers.views import CustomerViewSet, create_customer, register_user
from apps.flights.views import FlightViewSet, flights_list
from apps.planes.views import PlaneViewSet

router = DefaultRouter()
router.register(r"bookings", BookingViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"planes", PlaneViewSet)
router.register(r"flights", FlightViewSet)

urlpatterns = [
    path("", flights_list, name="flights_list"),
    path("customer/", create_customer, name="create_customer"),
    path("booking/<int:flight_id>/", create_booking, name="create_booking"),
    path("register/", register_user, name="register_user"),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
