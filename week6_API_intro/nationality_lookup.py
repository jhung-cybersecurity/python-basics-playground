import requests

while True:
    name = input("Enter your name: ")

    if name == "":
        print("You did not enter anything. Try again.")
    elif name == "quit":
        print("Terminal ended.")
        break 
    else:
        try:
            response = requests.get(f"https://api.nationalize.io/?name={name}")
            data = response.json()
            if not data["country"]:
                print("There's no country associated with this name.")
            else:
                print("Country:", data["country"][0]["country_id"])
                print("Probability:", data["country"][0]["probability"])
        except:
            print("Data Corrupted. Try again later.")


