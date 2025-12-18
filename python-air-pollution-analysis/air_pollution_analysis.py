import pandas as pd

# Load dataset
df = pd.read_csv("openaq_pm25.csv")

# Basic data cleaning
df_clean = df.drop_duplicates()
df_clean["value"] = pd.to_numeric(df_clean["value"], errors="coerce")
df_clean = df_clean.dropna(subset=["value"])

# Group by location and calculate metrics
df_result = (
    df_clean.groupby("location")["value"]
    .agg(["mean", "count"])
    .reset_index()
    .rename(columns={
        "mean": "average_pm25",
        "count": "records"
    })
    .sort_values(by=["records", "location"], ascending=[False, True])
)

# Display results
print(df_result.head())

