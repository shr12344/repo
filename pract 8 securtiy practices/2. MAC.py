#2. MAC : (Message Authentication Code)

import hmac, hashlib

key = b'shared_secret'
msg = b'Important Transaction: $500'
mac = hmac.new(key, msg, hashlib.sha256).hexdigest()

print("Message:", msg.decode())
print("MAC:", mac)

