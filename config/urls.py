from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.bookings.views import BookingViewSet
from apps.customers.views import CustomerViewSet
from apps.flights.views import FlightViewSet
from apps.planes.views import PlaneViewSet

router = DefaultRouter()
router.register(r"bookings", BookingViewSet)
router.register(r"customers", CustomerViewSet)
router.register(r"planes", PlaneViewSet)
router.register(r"flights", FlightViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls")),
]
