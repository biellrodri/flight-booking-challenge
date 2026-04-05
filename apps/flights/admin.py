from django.contrib import admin

from .models import Flight


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "departure_time", "plane")
    list_filter = ("origin", "destination", "departure_time")
    search_fields = ("origin", "destination")
