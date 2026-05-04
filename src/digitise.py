import pandas as pd

# Load raw digitised data
df = pd.read_csv("data/raw/raw_curve.csv")

# Rename columns
df.columns = ["time_s", "radius_um", "condition_id"]

# Remove missing rows
df = df.dropna()

# Within each condition id, sort by ascending time
df = df.sort_values(by=["condition_id", "time_s"])

# Ensure numeric types
df["time_s"] = pd.to_numeric(df["time_s"])
df["radius_um"] = pd.to_numeric(df["radius_um"])

# Save cleaned data
df.to_csv("data/processed/bubble_curves.csv", index=False)

print("Saved cleaned data to data/processed/bubble_curves.csv")