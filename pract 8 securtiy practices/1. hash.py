
#PRACTICAL 8: SECURITY PRACTICES
#1. HASH

import hashlib
message = "Hello Security Students"
hash_digest = hashlib.sha256(message.encode()).hexdigest()
print("SHA256 Hash:", hash_digest)
