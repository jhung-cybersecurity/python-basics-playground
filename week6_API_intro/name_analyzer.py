import requests

while True:
    name = input("Enter your name: ")

    if name == "":
        print("You didn't enter anything.")
    elif name == "quit":
        print("Terminal ended.")
        break
    else:
        try:
            response_nation = requests.get(f"https://api.nationalize.io/?name={name}")
            response_age = requests.get(f"https://api.agify.io/?name={name}")
            data_nation = response_nation.json() 
            data_age = response_age.json()

            if data_nation["country"]:
                probability = round(data_nation["country"][0]["probability"] * 100, 1)
                print("Top Country:", data_nation["country"][0]["country_id"], f"{probability}%")
            else:
                print("No Country.")

            if data_age["age"]:
                print("Predicted Age:", data_age["age"])
            else:
                print("No Age.")
        except:
            print("Data Corrupted. Close and try again.")

