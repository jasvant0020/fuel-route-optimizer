import pandas as pd
from pathlib import Path


class FuelService:

    _df = None

    @classmethod
    def load_data(cls):

        if cls._df is None:

            csv_path = (
                Path(__file__)
                .resolve()
                .parent.parent
                / "data"
                / "fuel-prices-for-be-assessment.csv"
            )

            cls._df = pd.read_csv(csv_path)

        return cls._df

    @classmethod
    def get_cheapest_station(cls):

        df = cls.load_data()

        station = df.loc[
            df["Retail Price"].idxmin()
        ]

        return station.to_dict()

    @classmethod
    def get_state_stations(cls, state):

        df = cls.load_data()

        return df[
            df["State"] == state
        ]