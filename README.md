<div align="center">

# 🛰️ PEER'S OSINT SCANNER
### *Passive Open-Source Intelligence & Reconnaissance Tool*

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Organization](https://img.shields.io/badge/Sqrock%20IT%20Solution-Cybersecurity-00C853?style=for-the-badge)](https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Developed by <a href="https://github.com/MdPeerSiddiqui">Md Peer Siddiqui</a> | Sqrock IT Solution Internship</b>
</p>

---

</div>

## 🖥️ Terminal Preview

```text
  ____  _____ _____ ____  ____     ___  ____ ___ _   _ _____ 
 |  _ \| ____| ____|  _ \/ ___|   / _ \/ ___|_ _| \ | |_   _|
 | |_) |  _| |  _| | |_) \___ \  | | | \___ \| ||  \| | | |  
 |  __/| |___| |___|  _ < ___) | | |_| |___) | || |\  | | |  
 |_|   |_____|_____|_| \_\____/   \___/|____/___|_| \_| |_|  
  ____   ____    _    _   _ _   _ _____ ____                 
 / ___| / ___|  / \  | \ | | \ | | ____|  _ \                
 \___ \| |     / _ \ |  \| |  \| |  _| | |_) |               
  ___) | |___ / ___ \| |\  | |\  | |___|  _ <                
 |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\               

 ⚡ PEER'S OSINT SCANNER v1.0 — Passive Reconnaissance Suite ⚡
 [★] Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Track
===========================================================================

[*] TARGET IDENTIFIED : example.com
[*] TARGET TYPE       : Domain Name
[*] TIME OF SCAN      : 2026-10-20 13:45:59 UTC
---------------------------------------------------------------------------

[1] RESOLVING DNS & HOST ROUTING...
    [+] Target Domain    : example.com
    [+] Resolved IPv4    : 104.20.23.154

[2] QUERYING WHOIS REGISTRATION INTELLIGENCE...
    [+] Registrar        : RESERVED-Internet Assigned Numbers Authority
    [+] Registered Date  : 1995-08-14 04:00:00+00:00
    [+] Expiration Date  : 2027-08-13 04:00:00+00:00
    [+] Name Servers     : ELLIOTT.NS.CLOUDFLARE.COM, HERA.NS.CLOUDFLARE.COM

[3] GEOLOCATION, ASN & INFRASTRUCTURE DATA...
    [+] Country          : Canada (CA)
    [+] City / Region    : Toronto, Ontario
    [+] Coordinates      : 43.6532, -79.3832
    [+] ISP Provider     : Cloudflare, Inc.
    [+] Organization     : Cloudflare, Inc.
    [+] AS Number        : AS13335 Cloudflare, Inc.
    [i] Security Posture : Cloudflare WAF / Reverse Proxy Protection

===========================================================================
                      ✔ SCAN COMPLETED SUCCESSFULLY
===========================================================================

[★] Structured JSON Report Saved  : reports/peers_scan_example.com.json
```

---

## ⚡ What Does This Tool Do?

**PEER'S OSINT Scanner** is a fast, lightweight, and 100% passive open-source reconnaissance script. It gathers intelligence on any **Domain Name** or **IP Address** without touching the target's internal servers:

* **Dual Target Detection**: Automatically identifies if you entered a Domain or an IP address.
* **DNS & Reverse Routing**: Resolves forward IPv4 A-records or performs reverse PTR lookups for raw IPs.
* **WHOIS Extraction**: Scrapes registrar, registration date, renewal/expiration date, and Name Servers.
* **Geolocation & ASN**: Maps physical location (Country, City, Coordinates), ISP, and Autonomous System Numbers.
* **Cloud & Proxy Detection**: Automatically flags Cloudflare WAF reverse proxies, AWS, and Google Cloud infrastructure.
* **Audit Deliverables**: Saves clean, structured JSON deliverables into the `reports/` folder.

---

## 🚀 How to Clone and Run (3 Simple Steps)

### Step 1: Clone the Repository
```bash
git clone https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner.git
cd Peers-Osint-Scanner
```

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```

### Step 3: Run the Scanner

#### Option A: Interactive Mode (Enter domain when prompted)
```bash
python peers_scanner.py
```

#### Option B: Direct Command
```bash
# Scan a domain
python peers_scanner.py example.com

# Or scan an IP address
python peers_scanner.py 8.8.8.8
```

---

## 📂 Repository Contents

```text
Peers-Osint-Scanner/
├── peers_scanner.py                # 🚀 The PEER'S OSINT Scanner tool
├── requirements.txt                # 📋 Python dependencies (requests, whois, colorama)
├── README.md                       # 📖 Tool documentation & quickstart
├── LICENSE                         # ⚖️ MIT Open Source License
└── reports/                        # 📊 Saved scan deliverables
    ├── peers_scan_example.com.json
    └── peers_scan_8.8.8.8.json
```

---

## 🏛️ Project Details
* **Author:** [Md Peer Siddiqui](https://github.com/MdPeerSiddiqui)
* **Organization:** Sqrock IT Solution
* **Internship Program:** Alpha 2 Internship — Cybersecurity Track
* **Phase:** Day 1 Practical Tool

---

## ⚖️ Legal & Ethical Policy
All intelligence gathering performed by this tool is strictly **passive** using public WHOIS and DNS records. It does not perform invasive port scans, exploitation, or intrusive network requests.
