from django.contrib import admin

from .models import Plane


@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "total_seats")
