from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="fuel_optimizer")


def get_coordinates(location):

    result = geolocator.geocode(location)

    if not result:
        raise ValueError(
            f"Location not found: {location}"
        )

    return result.latitude, result.longitude