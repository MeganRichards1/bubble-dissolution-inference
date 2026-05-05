import pandas as pd

# Load raw digitised data
df = pd.read_csv("data/raw/raw_curve.csv")
condition_names = [val for i, val in enumerate(df.columns) if i % 2 == 0]

df = df.iloc[1:, :]  # Drop the first column which is just an index
n = df.shape[1] // 2

df_long = pd.concat(
    [
        pd.DataFrame({
            "time_s": df.iloc[:, i*2],
            "radius_um": df.iloc[:, i*2 + 1],
            "condition_id": condition_names[i]
        })
        for i in range(n)
    ],
    ignore_index=True
).dropna()


# Save cleaned data
df_long.to_csv("data/processed/bubble_curves.csv", index=False)

print("Saved cleaned data to data/processed/bubble_curves.csv")