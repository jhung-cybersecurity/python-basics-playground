import requests

while True:
    name = input("Enter a name: ")

    if name == "":
        print("You didn't enter a name.")
    elif name == "quit":
        print("Terminal ended.")
        break
    else:
        response = requests.get(f"https://api.agify.io/?name={name}")
        if response.status_code != 200:
            print(f"API returned an error: {response.status_code}")
        else:
            data = response.json()
            if data["age"] is not None:
                print("Predicted Age:", data["age"])
            else:
                print("No age.")

