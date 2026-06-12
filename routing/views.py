from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RouteRequestSerializer
from .services import OSRMService
from .geocoder import get_coordinates


class RouteAPIView(APIView):

    def post(self, request):

        serializer = RouteRequestSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        start = serializer.validated_data["start"]
        destination = serializer.validated_data["destination"]

        start_lat, start_lon = get_coordinates(start)
        end_lat, end_lon = get_coordinates(destination)

        route_data = OSRMService.get_route(
            start_lon,
            start_lat,
            end_lon,
            end_lat
        )

        route = route_data["routes"][0]

        distance_miles = (
            route["distance"] / 1609.34
        )

        return Response(
            {
                "start": start,
                "destination": destination,
                "distance_miles": round(
                    distance_miles, 2
                ),
                "geometry": route["geometry"],
            },
            status=status.HTTP_200_OK,
        )