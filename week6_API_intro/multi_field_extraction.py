import requests

name = input("Enter a name: ")

if name == "":
        print("You didn't enter a name.")
else:
    try: 
        file = requests.get(f"https://api.agify.io/?name={name}")
        data = file.json()
        if data["age"] == None:
            print("No age data found for that name.")
        else:
            print("Name:", data["name"], "Age:", data["age"], "Count:", data["count"])
    except: 
        print("Something went wrong. Try again.")


