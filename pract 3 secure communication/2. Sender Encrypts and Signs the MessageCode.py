#2. Sender Encrypts and Signs the MessageCode:

# pip install cryptography
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# ---------- 1. Generate Receiver Keys (if not already present) ----------

if not (os.path.exists("receiver_private_key.pem") and os.path.exists("receiver_public_key.pem")):
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub = priv.public_key()
    with open("receiver_private_key.pem","wb") as f:
        f.write(priv.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.TraditionalOpenSSL,
            serialization.NoEncryption()
        ))
    with open("receiver_public_key.pem","wb") as f:
        f.write(pub.public_bytes(
            serialization.Encoding.PEM,
            serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print("Receiver RSA keys generated and saved.")
else:
    print("Receiver keys already exist. Skipping regeneration.")

# ---------- 2. Sender Encrypts and Signs the Message ----------

# --- Encrypt & sign message ---
recv_pub = serialization.load_pem_public_key(open("receiver_public_key.pem","rb").read())
send_priv = serialization.load_pem_private_key(open("sender_private_key.pem","rb").read(), None)
msg = b"Confidential project submission due date: 30th July"

enc = recv_pub.encrypt(msg, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
sig = send_priv.sign(msg, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())

open("encrypted_message.bin","wb").write(enc)
open("signature.bin","wb").write(sig)
print("Message encrypted & signed.")
