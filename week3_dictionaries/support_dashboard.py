tickets = [
    {"customer_name": "  jerry  ", "issue": " Forgot Password ", "status": "open"},
    {"customer_name": " anna ", "issue": " Billing Question ", "status": "closed"},
    {"customer_name": " MIKE ", "issue": " Cannot log into email ", "status": "open"},
    {"customer_name": " tom ", "issue": " password reset ", "status": "open"}
]

def clean_ticket(ticket):
    return {
        "customer_name": ticket["customer_name"].strip().title(),
        "issue": ticket["issue"].strip(),
        "status": ticket["status"].strip().lower()
    }

def count_open_tickets(tickets):
    count = 0
    for ticket in tickets:
        if ticket["status"] == "open":
            count = count + 1
    return count

def find_password_tickets(tickets):
    count = 0
    for ticket in tickets:
        if "password" in ticket["issue"].lower():
            count = count + 1
    return count

cleaned_tickets = []

for ticket in tickets:
    cleaned_tickets.append(clean_ticket(ticket))

for ticket in cleaned_tickets:
    print(ticket["customer_name"], "-", ticket["issue"], "-", ticket["status"])

print("Open tickets:", count_open_tickets(cleaned_tickets))
print("Password-related tickets:", find_password_tickets(cleaned_tickets))