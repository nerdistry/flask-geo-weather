import requests

reponse = requests.get("http://ip-api.com/json/24.48.0.1")

print(reponse.content)
