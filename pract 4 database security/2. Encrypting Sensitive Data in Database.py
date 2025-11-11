#PRACTICAL 4: DATABASE SECURITY
#2. Encrypting Sensitive Data in Database

import sqlite3, bcrypt

# Setup database
conn = sqlite3.connect('secure_users.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

# Register user
user = input("Enter username: ")
pwd = input("Enter password: ")
hashed = bcrypt.hashpw(pwd.encode(), bcrypt.gensalt())
cur.execute("INSERT INTO users VALUES (?, ?)", (user, hashed))
conn.commit()

# Login
u = input("Username to login: ")
p = input("Password to login: ")
cur.execute("SELECT password FROM users WHERE username = ?", (u,))
data = cur.fetchone()

if data and bcrypt.checkpw(p.encode(), data[0]):
    print("Login successful!")
else:
    print("Login failed.")

conn.close()
