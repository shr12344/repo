#2. HMAC for Data Integrity

import hmac
import hashlib
# Secret key shared between IoT device and server
secret_key = b"iot_secret_key"

# IoT message
message = b"Humidity: 70%"

# Generate HMAC (sender side)
hmac_digest = hmac.new(secret_key, message, hashlib.sha256).hexdigest()
print("Message:", message.decode())
print("Generated HMAC:", hmac_digest)

# Receiver recomputes HMAC for verification
received_hmac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

# Compare safely
if hmac.compare_digest(hmac_digest, received_hmac):
    print("Message is authentic ")
else:
    print("Message tampered ")
