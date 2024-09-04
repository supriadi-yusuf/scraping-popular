import requests

source = requests.get('https://www.floatrates.com/daily/idr.json')
#print(source.status_code)

json_data = source.json()
print(json_data)