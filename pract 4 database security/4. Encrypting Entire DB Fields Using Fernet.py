#4. Encrypting Entire DB Fields Using Fernet

from cryptography.fernet import Fernet
# Generate a symmetric encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
message = "sensitive msg"
encrypted = cipher.encrypt(message.encode())

# Decrypt
decrypted = cipher.decrypt(encrypted).decode()


print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
