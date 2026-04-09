import json

file = open("support_data.json", "r")
tickets = json.load(file)
file.close()

open_count = 0
high_priority_count = 0

for ticket in tickets:
    print("Ticket:", ticket["id"], "| Customer:", ticket["customer"], "| Issue:", ticket["issue"])

    if ticket["status"] == "open":
        open_count += 1

    if ticket["priority"] == "high":
        high_priority_count += 1

print()
print("Open tickets:", open_count)
print("High priority tickets:", high_priority_count)

for ticket in tickets:
    if ticket["status"] == "open":
        print("Open ticket found:", ticket["id"])