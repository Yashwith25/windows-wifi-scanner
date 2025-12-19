# windows-wifi-scanner
Developed a Python tool to detect active devices on a local Wi-Fi network using IP scanning and ARP-based MAC detection.

📡 Windows Wi‑Fi Network Scanner (Python)

A simple Python-based network scanning tool for Windows that detects devices connected to the same Wi‑Fi network using IP scanning and ARP lookup.

This project demonstrates basic networking concepts such as IP addressing, subnet scanning, and MAC address detection.

🚀 Features

Detects active devices on the local network

Displays:

IP Address

MAC Address (if available)

Automatically detects the local subnet

Clean, readable terminal output

Works on Windows systems

🛠️ Technologies Used

Python 3

Windows networking commands (ping, arp)

Standard Python libraries (subprocess, ipaddress, socket)

📌 How It Works (Brief)

The program detects your local IP address.

It calculates the subnet (e.g., 192.168.X.0/24).

Each IP in the range is pinged to check if it is online.

The ARP table is checked to retrieve MAC addresses.

Results are displayed in a formatted table.

📷 Sample Output (Privacy‑Safe)

⚠️ Note: The following output uses redacted / sample IP and MAC addresses to protect privacy.

============================================================
          Windows Wi-Fi Network Scanner
============================================================

My IP Address: X.X.X.X

Scanning Network: 192.168.X.0/24

------------------------------------------------------------
[ONLINE] IP: 192.168.X.1    | MAC: AA-BB-CC-DD-EE-FF
[ONLINE] IP: 192.168.X.7    | MAC: 11-22-33-44-55-66
[ONLINE] IP: X.X.X.X        | MAC: Unknown

------------------------------------------------------------
Scan Completed
------------------------------------------------------------

IP Address       | MAC Address
-----------------------------------
192.168.X.1      | AA-BB-CC-DD-EE-FF
192.168.X.7      | 11-22-33-44-55-66
X.X.X.X          | Unknown

------------------------------------------------------------
Total Devices Online: 3
------------------------------------------------------------

