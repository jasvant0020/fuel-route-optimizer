from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import FuelService

@api_view(["GET"])
def cheapest_station(request):
    data = FuelService.get_cheapest_station()
    return Response(data)

@api_view(["GET"])
def stations_by_states(request):
    states_param = request.GET.get("states", "")

    if not states_param:
        return Response(
            {"error": "states query param is required"},
            status=400
        )

    states = [s.strip().upper() for s in states_param.split(",")]

    df = FuelService.load_data()

    valid_states = set(df["State"].unique())
    invalid = [s for s in states if s not in valid_states]

    if invalid:
        return Response({
            "error": "Invalid states provided",
            "invalid_states": invalid,
            "available_states": sorted(list(valid_states))
        }, status=400)

    result = df[df["State"].isin(states)]

    if result.empty:
        return Response(
            {"message": "No stations found for given states"},
            status=404
        )

    return Response(result.to_dict(orient="records"))

@api_view(["GET"])
def available_states(request):
    df = FuelService.load_data()

    return Response({
        "states": sorted(df["State"].unique().tolist())
    })