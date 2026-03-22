from rest_framework import viewsets

from .models import Plane
from .serializers import PlaneSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer
