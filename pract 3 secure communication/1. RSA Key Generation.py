#PRACTICAL 3- SECURE COMMUNICATION
#1. RSA Key Generation (Sender & Receiver) Code:


# Import the required libraries
from cryptography.hazmat.primitives.asymmetric import rsa   # used to create RSA keys
from cryptography.hazmat.primitives import serialization     # used to save keys

# Step 1: Generate the sender's private key
priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Step 2: Generate the sender's public key from the private key
pub = priv.public_key()

# Step 3: Save the private key in a file
# (No password or encryption used for simplicity)
open("sender_private_key.pem", "wb").write(priv.private_bytes(
    serialization.Encoding.PEM,                   # file format type
    serialization.PrivateFormat.TraditionalOpenSSL, # how key is stored, SSL =Secure Socket Layer
    serialization.NoEncryption()                  # no password
))

# Step 4: Save the public key in a file
open("sender_public_key.pem", "wb").write(pub.public_bytes(
    serialization.Encoding.PEM,                   # file format type
    serialization.PublicFormat.SubjectPublicKeyInfo # how key is stored
))

# Step 5: Print confirmation message
print("RSA keys generated and saved.")
