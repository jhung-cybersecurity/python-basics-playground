import requests

name = input("Enter a name: ")

file = requests.get(f"https://api.agify.io/?name={name}")

data = file.json()

print("Age:", data["age"])


