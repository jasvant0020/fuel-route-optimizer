import pandas as pd
from pathlib import Path
from functools import lru_cache


class FuelService:

    @staticmethod
    @lru_cache(maxsize=1)
    def load_data():

        csv_path = (
            Path(__file__)
            .resolve()
            .parent.parent
            / "data"
            / "fuel-prices-for-be-assessment.csv"
        )

        df = pd.read_csv(csv_path)

        # -----------------------------
        # VALIDATION (IMPORTANT)
        # -----------------------------
        required_columns = {"Retail Price", "State"}

        missing = required_columns - set(df.columns)

        if missing:
            raise ValueError(f"Missing required columns: {missing}")

        return df

    @classmethod
    def get_cheapest_station(cls):

        df = cls.load_data()

        station = df.loc[df["Retail Price"].idxmin()]

        return station.to_dict()

    @classmethod
    def get_stations_by_states(cls, states):

        df = cls.load_data()

        # Normalize input (VERY IMPORTANT)
        states = [s.strip().upper() for s in states]

        return df[df["State"].isin(states)]