from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .services import FuelService
from .pagination import FuelPagination

class FuelViewSet(ViewSet):

    def cheapest(self, request):
        data = FuelService.get_cheapest_station()
        return Response(data)
    
    def stations(self, request):
        df = FuelService.load_data()

        # -----------------------------
        # FILTER: states
        # -----------------------------
        states_param = request.GET.get("states")
        if states_param:
            states = [s.strip().upper() for s in states_param.split(",")]
            df = df[df["State"].isin(states)]

        # -----------------------------
        # FILTER: price range
        # -----------------------------
        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")

        if min_price:
            df = df[df["Retail Price"] >= float(min_price)]

        if max_price:
            df = df[df["Retail Price"] <= float(max_price)]

        # -----------------------------
        # SORTING
        # -----------------------------
        ordering = request.GET.get("ordering")

        if ordering == "price":
            df = df.sort_values("Retail Price", ascending=True)
        elif ordering == "-price":
            df = df.sort_values("Retail Price", ascending=False)

        # -----------------------------
        # PAGINATION (NEW)
        # -----------------------------
        paginator = FuelPagination()

        result_page = paginator.paginate_queryset(
            df.to_dict(orient="records"),
            request
        )

        return paginator.get_paginated_response(result_page)