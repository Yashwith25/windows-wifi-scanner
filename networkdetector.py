import subprocess
import ipaddress
import re
import threading

# -------------------------
# ANSI COLOR CODES
# -------------------------
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

# -------------------------
# GLOBAL VARIABLES
# -------------------------
active_devices = []
lock = threading.Lock()

# -------------------------
# FUNCTION: Ping an IP
# -------------------------
def ping_ip(ip):
    """Ping an IP address"""
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "180", ip],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    return "TTL=" in result.stdout

# -------------------------
# FUNCTION: Get MAC address
# -------------------------
def get_mac(ip):
    """Get MAC address from ARP table"""
    try:
        arp_output = subprocess.check_output(["arp", "-a"], text=True)
        pattern = rf"{ip}\s+([a-fA-F0-9-]{{17}})"
        match = re.search(pattern, arp_output)
        return match.group(1) if match else "Unknown"
    except:
        return "Unknown"

# -------------------------
# FUNCTION: Scan a single IP
# -------------------------
def scan_ip(ip):
    """Scan a single IP"""
    if ping_ip(ip):
        mac = get_mac(ip)
        with lock:
            active_devices.append((ip, mac))
            print(f"{GREEN}[ONLINE]{RESET} IP: {ip:<15} | MAC: {mac}")

# -------------------------
# FUNCTION: Get Wi-Fi IP
# -------------------------
def get_wifi_network():
    """Get local Wi-Fi IPv4 address"""
    output = subprocess.check_output("ipconfig", text=True)
    match = re.search(r"Wireless LAN adapter.*?IPv4 Address.*?:\s*([\d\.]+)", output, re.S)
    
    if match:
        return match.group(1)
    else:
        print(f"{RED}❌ No Wi-Fi IPv4 address found. Are you connected to Wi-Fi?{RESET}")
        exit()

# =========================
# MAIN SCRIPT
# =========================
print("\n" + "="*60)
print("          Windows Wi-Fi Network Scanner")
print("="*60 + "\n")

# 1. Get your Wi-Fi IP
my_ip = get_wifi_network()
print(f"My IP Address: {my_ip}\n")

# 2. Define /24 network
network = ipaddress.ip_network(my_ip + "/24", strict=False)
print(f"Scanning Network: {network}\n")
print("-"*60)

# 3. Scan all IPs in the network using threads
threads = []
for ip in network:
    ip = str(ip)
    if ip.endswith(".0") or ip.endswith(".255"):
        continue  # Skip network & broadcast

    t = threading.Thread(target=scan_ip, args=(ip,))
    threads.append(t)
    t.start()

# 4. Wait for all threads to finish
for t in threads:
    t.join()

# 5. Show summary
print("\n" + "-"*60)
print(f"{CYAN}Scan Completed{RESET}")
print("-"*60 + "\n")

if active_devices:
    print(f"{'IP Address':<16} | {'MAC Address'}")
    print("-"*35)
    for ip, mac in active_devices:
        print(f"{ip:<16} | {mac}")
else:
    print("No active devices found on the network.")

print("\n" + "-"*60)
print(f"Total Devices Online: {len(active_devices)}")
print("-"*60 + "\n")
