import pandas as pd
import numpy as np
import json

csv = pd.read_csv('skadnetwork_id.csv', keep_default_na=False)

title = csv.columns.values
data = csv.values
print(title)
# print(data)
# exit()

ids_dict = {"skadnetwork_ids": []}

for idx, row in enumerate(data):
    # if pd.isna(row[1]):
    #     continue

    if row[1] == '':
        continue
    new_row = {
        "entity_name": row[0],
        "entity_domain": row[1],
        "skadnetwork_id": row[2],
        "creation_date":"2023-05-15T00:00:00Z"
    }
    ids_dict["skadnetwork_ids"].append(new_row)
    # if idx == 1:
    #     break

# print(json.dumps(ids_dict))

ids2_dict = {"skadnetwork_ids": []}
csv2 = pd.read_csv('skadnetwork_id2.csv', header=0, keep_default_na=False)
data = csv2.values
for idx, row in enumerate(data):
    new_row_2 = {
        "skadnetwork_id": row[0]
    }
    ids2_dict["skadnetwork_ids"].append(new_row_2)

print(json.dumps(ids2_dict))