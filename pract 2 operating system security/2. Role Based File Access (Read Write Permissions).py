#2. Role-Based File Access (Read/Write Permissions)

permissions = {
"admin": ["read", "write"],
"user1": ["read"]
}

def access_file(user_role, action):
    if action in permissions.get(user_role, []):
        print(f"{user_role} can {action} the file ")
    else:
        print(f"{user_role} cannot {action} the file ")

access_file("admin", "write")
access_file("user1", "write")
