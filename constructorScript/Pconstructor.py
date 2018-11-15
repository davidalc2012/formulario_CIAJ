import json
with open('scheme.json') as file:
    scheme = file.read()

print(json.loads(scheme)['a'])
