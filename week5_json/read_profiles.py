import json

file = open("profiles.json", "r")
profiles = json.load(file)
file.close()

support_count = 0

for profile in profiles:
    print("Name:", profile["name"])
    print("Department:", profile["department"])
    print("Tickets Closed", profile["stats"]["tickets_closed"])
    print("Rating", profile["stats"]["rating"])
    print()

    if profile["department"] == "Support":
        support_count += 1

for ticket_closed in profiles:
    if ticket_closed["stats"]["tickets_closed"] > 10:
        print("Top closer:", ticket_closed["name"])
