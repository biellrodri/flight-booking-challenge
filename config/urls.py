from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.bookings.views import BookingViewSet
from apps.customers.views import CustomerViewSet

router = DefaultRouter()
router.register(r"bookings", BookingViewSet)
router.register(r"customers", CustomerViewSet)

urlpatterns = [path("admin/", admin.site.urls), path("api/", include(router.urls))]
