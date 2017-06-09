import requests
from api_key import api_key

veid ='293750'
base_url = 'https://api.64clouds.com/v1/getServiceInfo?'

params = {
    'veid': veid,
    'api_key': api_key,
}

r = requests.get(base_url, params=params)

print(type(r.json()))
