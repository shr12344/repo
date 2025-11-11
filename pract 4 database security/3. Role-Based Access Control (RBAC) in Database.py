#3. Role-Based Access Control (RBAC) in Database

import sqlite3

# Connect to database and create table
c = sqlite3.connect('rbac.db'); cur = c.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT, role TEXT)")

# Add sample users if not present
cur.execute("SELECT 1 FROM users WHERE username='admin'")
if not cur.fetchone():
    cur.executemany("INSERT INTO users VALUES(?,?,?)",
                    [('admin','admin123','admin'), ('john','john123','student')])
    c.commit()

# Login input
u, p = input("Username: "), input("Password: ")

# Check credentials
cur.execute("SELECT role FROM users WHERE username=? AND password=?", (u, p))
r = cur.fetchone()

# Grant access based on role
if r:
    print(f"Login successful! Role: {r[0]}")
    print("Access granted to view, add, delete, modify records" if r[0]=='admin' else "Granted access to View records only" if r[0]=='student' else "Limited access")
else:
    print("Invalid credentials.")

c.close()  # Close connection

