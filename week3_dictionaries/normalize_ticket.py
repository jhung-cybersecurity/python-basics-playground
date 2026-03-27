ticket = {
    "customer_name": "  jErry  ",
    "issue": " Forgot Password ",
    "status": " Open "
}

clean_name = ticket["customer_name"].strip().title()
clean_issue = ticket["issue"].strip()
clean_status = ticket["status"].strip().lower()

print("Customer Name:", clean_name)
print("Issue:", clean_issue)
print("Status:", clean_status)