import scapy.all as scapy
import sys

# Windows ke liye layer 3 par switch karne ka sahi tarika
try:
    from scapy.arch.windows import WindowsLibpcapSocket
    scapy.conf.L3socket = WindowsLibpcapSocket
except ImportError:
    pass

def process_packet(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"[+] Packet: {ip_src} -> {ip_dst}")

def start_sniffing():
    print("[*] Starting Sniffer...")
    # iface=None se ye khud best interface select karega
    scapy.sniff(store=False, prn=process_packet)

if __name__ == "__main__":
    try:
        start_sniffing()
    except Exception as e:
        print(f"[-] Error: {e}")