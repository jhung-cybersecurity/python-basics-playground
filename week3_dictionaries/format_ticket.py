ticket = {
    "customer_name": "Jerry",
    "issue": "Forgot password",
    "status": "open"
}

def format_ticket(ticket):
    return ticket["customer_name"] + " - " + ticket["issue"] + " - " + ticket["status"]

print(format_ticket(ticket))

