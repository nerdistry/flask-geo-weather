import requests

response = requests.get("http://ip-api.com/json/24.48.0.1").json()


print(response['lat'])
print(response['lon'])