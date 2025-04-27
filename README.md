# 🔍 Multi Port Scanner

A Python-based TCP port scanner that allows scanning single ports, multiple ports, or a range of ports on a target domain or IP. It includes DNS resolution, port validation, timeout handling, and basic error reporting.

## 🚀 Features

- Scan:
  - A **single** TCP port
  - A **list** of comma-separated ports
  - A **range** of ports (e.g., 20-80)
- DNS resolution of domain names to IP
- Timeout and error handling for different port states (open, closed, filtered)
- Port input validation (range: 0–65535)

## 🛠️ How It Works

1. The script resolves the domain name to an IP address.
2. It validates the port(s) given by the user.
3. Attempts TCP connection to each port.
4. Displays the result:
   - ✅ Open
   - ⛔ Closed
   - 🚫 Filtered (no response)

## 🧪 Example Usage

~~~bash
$ python3 multi_port_scanner.py
Enter domain: example.com
Enter ports (Eg: 21,22,80 or 21-25 or 80): 21, 22, 25
~~~

## 📦 Requirements
Python 3.x (standard libraries only – no external dependencies)

##📁 File Structure

multi_port_scanner/
└── multi_port_scanner.py

## 📌 Notes
This script only scans TCP ports.

UDP scanning is not yet supported.

Timeout is currently set to 2 seconds per port.