ticket = {
    "customer_name": "Jerry",
    "issue": "Forgot email login password",
    "priority": "Medium",
    "status": "Open",
}

print("Customer Name:", ticket["customer_name"])
print("Issue:", ticket["issue"])
print("Priority:", ticket["priority"])
print("Status:", ticket["status"])

if ticket["priority"].lower() == "high" and ticket["status"].lower() == "open":
    print("Handle immediately")
elif ticket["priority"].lower() == "medium" and ticket["status"].lower() == "open":
    print("Handle soon")
elif ticket["status"].lower() == "closed":
    print("Ticket already resolved")
else:
    print("Normal queue")