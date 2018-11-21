import json
from pprint import pprint

with open('../schemeExamples/schemeEx1') as f:
    data = json.load(f)

pprint(data)
print(data['date'])
print(data['question'][0])
print(data['question'][0]['text'])