import requests


class OSRMService:

    BASE_URL = "https://router.project-osrm.org"

    @classmethod
    def get_route(cls, start_lon, start_lat, end_lon, end_lat):

        url = (
            f"{cls.BASE_URL}/route/v1/driving/"
            f"{start_lon},{start_lat};"
            f"{end_lon},{end_lat}"
            "?overview=full&geometries=geojson"
        )

        response = requests.get(url)
        response.raise_for_status()

        return response.json()