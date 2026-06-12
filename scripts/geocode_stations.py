import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim(
    user_agent="fuel_optimizer"
)

df = pd.read_csv(
    "data/fuel-prices-for-be-assessment.csv"
)

df["latitude"] = None
df["longitude"] = None