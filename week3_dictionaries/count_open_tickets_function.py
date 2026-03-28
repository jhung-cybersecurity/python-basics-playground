tickets = [
    {"customer_name": "Jerry", "issue": "Forgot password", "status": "open"},
    {"customer_name": "Tom", "issue": "Monitor won't turn on", "status": "open"},
    {"customer_name": "Brady", "issue": "Lost my keyboard", "status": "open"},
    {"customer_name": "Tommie", "issue": "Mouse won't work", "status": "open"}
]

def count_open_tickets(tickets):
    count = 0

    for ticket in tickets:
        if ticket["status"] == "open":
            count = count + 1

    return count

print("Total open tickets:", count_open_tickets(tickets))