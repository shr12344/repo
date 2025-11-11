#4. Packet Sniffing in IoT Traffic

from scapy.all import sniff
# Callback function to process each captured packet
def packet_callback(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        print(f"[IP Packet] {src} → {dst}")


    if packet.haslayer("Raw"):  # Application data
        payload = packet["Raw"].load
        print("Payload:", payload)


print("Sniffing IoT traffic... Press Ctrl+C to stop")


# Capture 10 packets (increase count for live demo)
sniff(prn=packet_callback, count=10)
