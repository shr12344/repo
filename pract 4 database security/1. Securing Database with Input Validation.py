#PRACTICAL 4: DATABASE SECURITY
#1. Securing Database with Input Validation

import sqlite3

with sqlite3.connect('student.db') as conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    cur.execute("INSERT OR IGNORE INTO users VALUES('admin','admin123')")
    conn.commit()

u = input("Enter username: ")
p = input("Enter password: ")
cur.execute("SELECT 1 FROM users WHERE username=? AND password=?", (u, p))
print("Login successful!" if cur.fetchone() else "Invalid credentials.")
