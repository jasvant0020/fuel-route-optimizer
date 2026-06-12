from rest_framework.views import APIView
from rest_framework.response import Response

from .services import FuelService


class CheapestFuelAPIView(APIView):

    def get(self, request):

        station = (
            FuelService.get_cheapest_station()
        )

        return Response(station)