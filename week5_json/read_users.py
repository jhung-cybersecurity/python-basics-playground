import json

file = open("users.json", "r")
users = json.load(file)
file.close()

active_count = 0

for user in users:
    print(user["name"])

    if user["active"] == True:
        active_count += 1

print("Active users:", active_count)

for user in users:
    if user["role"] == "admin":
        print("Admin user:", user["name"])