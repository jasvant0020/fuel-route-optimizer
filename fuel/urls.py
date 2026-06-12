from django.urls import path

from .views import CheapestFuelAPIView

urlpatterns = [
    path("cheapest/",CheapestFuelAPIView.as_view())
]