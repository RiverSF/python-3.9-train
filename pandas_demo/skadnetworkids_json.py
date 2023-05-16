import json

import pandas as pd

json_obj = pd.read_json("skadnetworkids.json", orient='columns')
title = json_obj.columns.values
json_obj = pd.read_json("skadnetworkids.json", orient='index')
data = json_obj.values
# print(title)
# exit()

new_json = {}
new_list = []
count = 0

for idx, row in enumerate(data):
    if idx == 3:
        print(len(row[0]))
        new_json[title[idx]] = []
        skadnetwork_ids = row[0]
        for idx2, item in enumerate(skadnetwork_ids):
            if item['skadnetwork_id'] in new_list:
                # print(idx2, item['skadnetwork_id'])
                continue
            new_list.append(item['skadnetwork_id'])
            if 'creation_date' in item:
                count += 1
                item['creation_date'] = "2023-05-15T00:00:00Z"
            new_json[title[idx]].append(item)
            # print(new_json)
            # exit()
    else:
        new_json[title[idx]] = row[0]

print(json.dumps(new_json))


dfj = pd.DataFrame(new_json)
dfj.to_json("new_skadnetworkids.json", orient='records')