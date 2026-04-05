import json

file = open("tickets.json", "r")
tickets = json.load(file)
file.close()

open_count = 0
high_count = 0

for ticket in tickets:
    print("Ticket ID:", ticket["id"], "| Customer:", ticket["customer"])

    if ticket["status"] == "open":
        open_count += 1

    if ticket["priority"] == "high":
        high_count += 1

print("Open tickets:", open_count)
print("High priority tickets:", high_count)

for open_ticket in tickets:
    if open_ticket["status"] == "open":
        print("Open ticket found:", open_ticket["id"])