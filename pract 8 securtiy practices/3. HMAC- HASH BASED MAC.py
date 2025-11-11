#3. HMAC (Hash-based MAC)

import hmac, hashlib
key = b'super_secret_key'
msg = b'Authenticate this message'
print("HMAC:", hmac.new(key, msg, hashlib.sha256).hexdigest())



