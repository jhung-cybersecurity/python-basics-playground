issue = "Customer cannot log into email"
issue_lower = issue.lower()

if "email" in issue_lower:
    print("This is an email-related issue")
elif "password" in issue_lower:
    print("This may be a password issue")
else:
    print("General support issue")