import json
import os
from os import path
data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})
fileArray = os.listdir()
print(x[5])
print()
for x in fileArray:
    if(x.)
with open('C:/Users/Salem/Desktop/Pytest/data.json', 'w') as outfile:
    json.dump(data, outfile)