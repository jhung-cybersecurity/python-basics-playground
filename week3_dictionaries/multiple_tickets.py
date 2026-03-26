tickets = [
    {
        "customer_name": "Jerry",
        "issue": "Forgot password",
        "priority": "high",
        "status": "open"
    },
    {
        "customer_name": "Anna",
        "issue": "Billing question",
        "priority": "medium",
        "status": "closed"
    },
    {
        "customer_name": "Mike",
        "issue": "Cannot access portal",
        "priority": "low",
        "status": "open"
    }
]

for ticket in tickets:
    print("Customer Name:", ticket["customer_name"])
    print("Issue:", ticket["issue"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket["status"])
    print()