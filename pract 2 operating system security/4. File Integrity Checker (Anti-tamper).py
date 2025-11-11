#4. File Integrity Checker (Anti-tamper)

import hashlib

def get_file_hash(filename):
    with open(filename, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()
 
original_hash = get_file_hash("sample.txt")
current_hash = get_file_hash("sample2.txt")

if original_hash == current_hash:
    print(" File is intact")
else:
    print(" File has been changed!")
