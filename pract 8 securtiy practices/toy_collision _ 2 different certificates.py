#PRACTICAL 8: SECURITY PRACTICES
# toy_collision_demo.py
# Educational demo: two different "certificate" byte-strings that produce the same value

def toy_hash(b: bytes) -> int:
    return sum(b) % 256

def make_base_certs():
    c1 = b"""-----BEGIN CERTIFICATE-----
Subject: CN=Alice Example
Issuer: Test CA
PublicKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCu
-----END CERTIFICATE-----
"""
    c2 = b"""-----BEGIN CERTIFICATE-----
Subject: CN=Bob Example
Issuer: Test CA
PublicKey: AAAAB3NzaC1yc2EAAAADAQABAAABAQCu
-----END CERTIFICATE-----
"""
    return c1, c2

def pad_to_match(target, data):
    need = (target - sum(data) % 256) % 256
    return b'' if need == 0 else bytes([need])

def show_tail(b): return b[-40:].hex()

def main():
    cert1, cert2 = make_base_certs()
    h1, h2 = toy_hash(cert1), toy_hash(cert2)
    print("Initial toy hashes:")
    print(" cert1 hash:", h1)
    print(" cert2 hash:", h2)
    print()

    padding = pad_to_match(h1, cert2)
    cert2_padded = cert2 + b"\n#PAD:" + padding
    h2_after = toy_hash(cert2_padded)

    print("After padding cert2:")
    print(" cert1 length:", len(cert1), "hash:", toy_hash(cert1))
    print(" cert2_padded length:", len(cert2_padded), "hash:", h2_after)
    print()
    print("Are bytes identical?:", cert1 == cert2_padded)
    print("Do they collide under toy_hash?:", toy_hash(cert1) == toy_hash(cert2_padded))
    print()
    print("tail(cert1)   (hex):", show_tail(cert1))
    print("tail(cert2_p) (hex):", show_tail(cert2_padded))

    with open("cert1_demo.pem", "wb") as f: f.write(cert1)
    with open("cert2_demo_padded.pem", "wb") as f: f.write(cert2_padded)

    print("\nWrote cert1_demo.pem and cert2_demo_padded.pem to disk (different files).")
    print("You can show students: files differ, but toy_hash(...) is the same.")

if __name__ == "__main__":
    main()
