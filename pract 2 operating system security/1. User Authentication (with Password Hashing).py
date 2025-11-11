#PRACTICAL 2: OPERATING SYSTEM SECURITY
#1. User Authentication (with Password Hashing)

import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    users[username] = hash_password(password)
    print("Registered Successfully!")

def login(username, password):
    if users.get(username) == hash_password(password):
        print("Access Granted!")
    else:
        print("Access Denied!")


register("admin", "securepass")
login("admin", "securepass")
login("admin", "wrongpass")


