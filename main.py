import numpy as np
import pandas as pd
import os
import glob

all_data = []
for f in glob.glob("C:/Users/emmanuelk/Desktop/excel/final/csv 0158-0192/*.csv"):
    all_data.append(pd.read_csv(f))

df = pd.concat(all_data, ignore_index=True)

period_data = df["PERIOD"].unique()

for i in period_data:
    a = df[df["PERIOD"].str.contains(i.strip())]
    a.to_excel(f"I:/CREDIT/CREDIT ADMIN/PCA Batch Schedules/GTP-2022/Emmanuel/Payment reconciliation for periods Jan Feb & March 2022/{i.strip()}.xlsx", index=False)

print(df)
