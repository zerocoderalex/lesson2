import requests
import pprint

params = {'q':'html'}

response = requests.get("https://api.github.com/search/repositories", params=params)

print(response.status_code)
response_json = response.json()

pprint.pprint(response_json)
