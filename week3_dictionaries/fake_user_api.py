users = [
    {"id": 1, "name": "Johnny", "role": "student"},
    {"id": 2, "name": "Anna", "role": "admin"},
    {"id": 3, "name": "Mike", "role": "student"}
]

for user in users:
    if user["role"] == "student":
        print(user["name"], "-", user["role"])