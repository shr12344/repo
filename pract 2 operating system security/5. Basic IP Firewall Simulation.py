#5. Basic IP Firewall Simulation

blocked_ips = ["192.168.1.100", "10.0.0.5"]

def check_access(ip):
    if ip in blocked_ips:
        print(f"Access denied for {ip}")
    else:
        print(f"Access granted for {ip}")
        
check_access("192.168.1.100")
check_access("8.8.8.8")
