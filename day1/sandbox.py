import json
import re

i = open('data.json')
##a = re.findall("\d+", i)
a = []
b = []

for j in i:
    print(re.match(r"\d+", j))
    a.append(re.match(r"\d+", j))


for number in a:
    print(number)

for h in a:
    for k in a:
        if(h is not None and k is not None):
            if(int(h) + int(k) == 2020):
                print(h * k)
