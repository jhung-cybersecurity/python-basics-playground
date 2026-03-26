tickets = [
    {
        "customer_name": "Bob",
        "issue": "Cannot log into email",
        "priority": "medium",
        "status": "open"
    },
    {
        "customer_name": "Jane",
        "issue": "Phone system is down",
        "priority": "high",
        "status": "open"
    },
    {
        "customer_name": "Claudia",
        "issue": "Cannot clock in",
        "priority": "low",
        "status": "open"
    },
    {
        "customer_name": "Ivy",
        "issue": "Internet is down",
        "priority": "high",
        "status": "closed"
    },
]

open_count = 0

for ticket in tickets:
    if ticket["status"] == "open":
        print(ticket["customer_name"], "has an open ticket about", ticket["issue"])
        open_count = open_count + 1

print("Total open tickets:", open_count)