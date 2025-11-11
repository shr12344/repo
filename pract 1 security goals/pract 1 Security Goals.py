#PRACT 1 Security Goals


#1. Confidentiality – Using Encryption (AES)
#Encrypt & Decrypt a Message using cryptography module


from cryptography.fernet import Fernet
# Generate a symmetric encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
message = "Top Secret Message!"
encrypted = cipher.encrypt(message.encode())

# Decrypt
decrypted = cipher.decrypt(encrypted).decode()

print("Key:", key.decode())
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)

#------------------------------------------------------------------------------------------------------------

#2.Integrity – Using Hashing (SHA-256)
#Check if file or message is tampered

print("x-" * 30)
import hashlib
# Original data
data = "This is important"
hash1 = hashlib.sha256(data.encode()).hexdigest()

# Simulate tampered data
tampered = "This is IMPORTANT"
hash2 = hashlib.sha256(tampered.encode()).hexdigest()

print("\nHash1:", hash1)
print("Hash2:", hash2)
print("Integrity Verified?" , hash1 == hash2)

#------------------------------------------------------------------------------------------------------------


#3. Availability – Simple Backup Script 
# Backup a file automatically

import shutil
# Backup file
original_file = 'data.txt'
backup_file = 'backup_data.txt'

shutil.copyfile(original_file, backup_file)
print("Backup completed!")

#------------------------------------------------------------------------------------------------------------

#4. Authentication – Username & Password Check 
#Simple authentication system


users = {
'admin': 'password123', # In real life, never store passwords like this!
'user1': 'hello123'
}

username = input("Enter username: ")
password = input("Enter password: ")

if users.get(username) == password:
    print("Access granted")
else:
    print("Access denied")

#------------------------------------------------------------------------------------------------------------

#5. Non-Repudiation – Digital Signature Simulation 
#Sign and verify message (simplified)

import hashlib
# Sender signs the message using a hash
message = "Approve $5000 transfer"
signature = hashlib.sha256(message.encode()).hexdigest()

# Receiver verifies
received_message = "Approve $5000 transfer"
received_signature = hashlib.sha256(received_message.encode()).hexdigest()

print("Signature Verified:", signature == received_signature)

#------------------------------------------------------------------------------------------------------------

#6. Accountability – Logging user actions 
#Example: Simple log system

import datetime
def log_action(user, action):
    with open("audit_log.txt", "a") as log:
        timestamp = datetime.datetime.now()
        log.write(f"{timestamp} - {user}: {action}\n")

log_action("admin", "Logged In")
log_action("user1", "Viewed Report")

