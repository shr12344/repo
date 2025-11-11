#3. File Encryption with AES

from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("encrypted.key", "wb") as filekey:
    filekey.write(key)
    
def encrypt_file(filename):
    with open("encrypted.key", "rb") as filekey:
        key = filekey.read()
        fernet = Fernet(key)
    
    with open(filename, "rb") as file:
        data = file.read()
        encrypted = fernet.encrypt(data)
        
    with open(filename, "wb") as file:
        file.write(encrypted)
        
        
print("File encrypted")
encrypt_file("sample.txt")
