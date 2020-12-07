import json
import re


with open('data.json', 'r') as data_file:
    json_data = data_file.read()

i = json.loads(json_data)
i = i["data"]


for h in i:
    for k in i:
        if(int(h) + int(k) == 2020):
            print(h * k)
