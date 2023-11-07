# python -m pip install requests
# python -m pip uninstall requests
# python -m venv venv
# source venv/bin/activate
# select interpreter venv

import requests

response = requests.get('http://api.open-notify.org/astros.json')

jsonResponse = response.json()

# print(jsonResponse)

print('The people currently in space:')
for person in jsonResponse['people']:
    print(person['name'])
