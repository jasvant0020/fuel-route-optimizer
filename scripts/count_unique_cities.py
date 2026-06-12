import pandas as pd

CSV_FILE = "data/fuel-prices-for-be-assessment.csv"

df = pd.read_csv(CSV_FILE)

unique_locations = (
    df[["City", "State"]]
    .drop_duplicates()
)

print(f"Total stations: {len(df)}")
print(f"Unique city/state combinations: {len(unique_locations)}")