from django.urls import path
from .viewsets import FuelViewSet

urlpatterns = [
    path("cheapest/", FuelViewSet.as_view({"get": "cheapest"})),
    path("stations/", FuelViewSet.as_view({"get": "stations"})),
]