# https://www.weatherapi.com/
# vlevchenko@live.com / lvn133
# api key fb536651417c4d9ab9a221907230611 https://www.weatherapi.com/

import requests


city = 'London'
url = 'https://api.weatherapi.com/v1/current.json?key=fb536651417c4d9ab9a221907230611&q='+city+'&aqi=no'

response = requests.get(url)
weatherJson = response.json()

temperature = weatherJson.get('current').get('temp_f')
description = weatherJson.get('current').get('condition').get('text')

print('Today\'s weather in ' + city + ' is', description, 'and', temperature, 'degrees')

