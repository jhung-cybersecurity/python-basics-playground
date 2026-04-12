import requests

while True:
    name = input("Enter a name: ")

    if name == "":
        print("You didn't enter a name. Try again.")
    elif name == "quit":
        print("Goodbye!")
        break
    else:
        try:
            response = requests.get(f"https://api.agify.io/?name={name}")
            data = response.json()
            if data["age"] is None:
                print("There's no age associated with this name. Try again.")
            else:
                print("Name:", data["name"], "Age:", data["age"], "Count:", data["count"])
        except:
            print("Data Corrupted.")



