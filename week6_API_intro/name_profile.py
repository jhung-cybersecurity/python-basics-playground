import requests

while True:
    name = input("Enter your name: ")
    
    if name == "":
        print("You didn't enter a name. Try again.")
    elif name == "quit":
        print("Terminal ended")
        break
    else:
        response_age = requests.get(f"https://api.agify.io/?name={name}")
        response_nationality = requests.get(f"https://api.nationalize.io/?name={name}")
        print("=============================")
        print("Profile for:", name)
        if response_age.status_code != 200:
            print(f"Age API error, Code: {response_age.status_code}")
        else:
            ## Age block
            data_age = response_age.json()
            if data_age["age"] is not None:
                print("Predicted Age: ", data_age["age"])
            else:
                print("There's no age associated with the name.")
        print("=============================")
        if response_nationality.status_code != 200:
            print(f"Nationality API error, Code: {response_nationality.status_code}")
        else:
            ## Nationality block
            data_nation = response_nationality.json()
            if not data_nation["country"]:
                print("There's no country associated with this name. Try again.")
            else:
                probability = round(data_nation["country"][0]["probability"] * 100, 1)
                print("Top Country: ", data_nation["country"][0]["country_id"], f"({probability}%)")
        print("=============================")



