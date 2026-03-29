users = [
    {"id": 1, "name": "Johnny", "role": "student"},
    {"id": 2, "name": "Anna", "role": "admin"},
    {"id": 3, "name": "Mike", "role": "student"}
]

def find_admin(users):
    for user in users:
        if user["role"] == "admin":
            return user["name"]
        
print(find_admin(users))
