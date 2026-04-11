import requests

file = requests.get("https://api.agify.io/?name=john")

data = file.json()

print("Age:", data["age"])

