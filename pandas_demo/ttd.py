import pandas as pd
import numpy as np

# df = pd.read_csv('ttd.csv', keep_default_na=False)
df = pd.read_excel('mw.xlsx', keep_default_na=False)
# print(df)

# title = df.columns.values
# data = df.values

sites = df['Site']
for idx, site in enumerate(sites):
    print(site)
