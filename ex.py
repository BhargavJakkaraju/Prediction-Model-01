import pandas as pd

df = pd.DataFrame({"date": ["2021-01-01", "2021-01-03", "2021-01-02"]})
df["date"] = pd.to_datetime(df["date"])
print(df.sort_values("date"))