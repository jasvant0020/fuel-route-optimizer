import math

from fuel.services import FuelService


class FuelOptimizer:

    VEHICLE_RANGE = 500
    MPG = 10

    @classmethod
    def calculate_trip(
        cls,
        distance_miles,
        states_crossed
    ):
        """
        Returns:
        {
            fuel_stops: [],
            gallons_needed: float,
            total_cost: float
        }
        """

        stations = FuelService.get_stations_by_states(
            states_crossed
        )

        if stations.empty:
            raise ValueError(
                "No fuel stations found."
            )

        stations = stations.sort_values(
            by="Retail Price"
        )

        gallons_needed = (
            distance_miles / cls.MPG
        )

        stops_needed = max(
            0,
            math.ceil(
                distance_miles / cls.VEHICLE_RANGE
            ) - 1
        )

        selected_stations = (
            stations.head(
                max(1, stops_needed)
            )
        )

        average_price = (
            selected_stations[
                "Retail Price"
            ].mean()
        )

        total_cost = (
            gallons_needed * average_price
        )

        fuel_stops = []

        for _, station in selected_stations.iterrows():

            fuel_stops.append(
                {
                    "name": station[
                        "Truckstop Name"
                    ],
                    "city": station[
                        "City"
                    ],
                    "state": station[
                        "State"
                    ],
                    "price": round(
                        station[
                            "Retail Price"
                        ],
                        3
                    ),
                }
            )

        return {
            "fuel_stops": fuel_stops,
            "gallons_needed": round(
                gallons_needed,
                2
            ),
            "total_cost": round(
                total_cost,
                2
            ),
        }