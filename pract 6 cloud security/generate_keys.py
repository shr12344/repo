#Secure File Upload and Access on Cloud with Encryption and Access Control
#2. generate keys

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("aes.key", "wb") as f:
    f.write(key)
print(" AES Key Generated")
