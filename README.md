<div align="center">

# 🛰️ PEER'S OSINT SCANNER
### *Automated Passive Reconnaissance & Intelligence Engine*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Track](https://img.shields.io/badge/Track-Cybersecurity%20Alpha%202-red?style=for-the-badge&logo=shield)](https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner)
[![Organization](https://img.shields.io/badge/Issuing%20Body-Sqrock%20IT%20Solution-00C853?style=for-the-badge)](https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner)
[![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)](LICENSE)

<p align="center">
  <b>Engineered by <a href="https://github.com/MdPeerSiddiqui">Md Peer Siddiqui</a> under Sqrock IT Solution — Alpha 2 Internship</b>
</p>

---

</div>

## 🖥️ Interactive Terminal Interface

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

**PEER'S OSINT Scanner** is an open-source, passive reconnaissance tool. It extracts critical intelligence on any **Domain Name** or **IP Address** without generating invasive alert traffic on target systems:

* 🌐 **Dual Target Detection**: Intelligently differentiates between FQDNs (e.g., `example.com`) and raw IP addresses (e.g., `93.184.215.14` or `8.8.8.8`).
* 📡 **DNS & Reverse Routing**: Resolves forward IPv4 A-records and performs reverse DNS PTR lookups.
* 📜 **Deep WHOIS Extraction**: Queries registrar data, registration timestamps, expiration windows, and authoritative Name Servers.
* 🌍 **Geolocation & ASN Metrics**: Maps geographic location (Country, City, Coordinates), ISP, and Autonomous System Numbers.
* 🛡️ **Passive Security Fingerprinting**: Automatically flags Cloudflare WAF reverse proxies, AWS, and Google Cloud infrastructure.
* 💾 **Automated Security Reports**: Auto-exports structured, audit-ready JSON deliverables to `reports/`.

---

## 🚀 Installation Guide (Cross-Platform)

### 🐧 Option 1: Linux / Kali Linux

Open your terminal and run:

```bash
# 1. Update package list and install git & python3-pip
sudo apt update && sudo apt install -y git python3 python3-pip python3-venv

# 2. Clone the repository
git clone https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner.git
cd Peers-Osint-Scanner

# 3. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the scanner
python3 peers_scanner.py
```

---

### 🪟 Option 2: Windows (PowerShell or Command Prompt)

Open PowerShell and run:

```powershell
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner.git
cd Peers-Osint-Scanner

# 2. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the scanner
python peers_scanner.py
```

---

### 🍎 Option 3: macOS (Apple Silicon / Intel)

Open Terminal and run:

```bash
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/Peers-Osint-Scanner.git
cd Peers-Osint-Scanner

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the scanner
python3 peers_scanner.py
```

---

## 🎮 How to Use

### 1. Interactive Mode (Prompts for target)
```bash
python peers_scanner.py
```
*Prompt:*
```text
[?] Enter Target Domain or IP Address (e.g. example.com)
    └── Target > example.com
```

### 2. Direct Command-Line Mode
```bash
# Scan a domain name (RFC 2606 lab domain)
python peers_scanner.py example.com

# Scan an IPv4 address directly
python peers_scanner.py 8.8.8.8
```

---

## 📂 Repository Contents

```text
Peers-Osint-Scanner/
├── peers_scanner.py                # 🚀 The PEER'S OSINT Scanner CLI Tool
├── requirements.txt                # 📋 Python dependencies (requests, python-whois, colorama)
├── README.md                       # 📖 Tool documentation & quickstart
├── LICENSE                         # ⚖️ MIT Open Source License
└── reports/                        # 📊 Saved scan deliverables
    ├── peers_scan_example.com.json
    └── peers_scan_8.8.8.8.json
```

---

## 🛡️ Attacker vs. Defender Security Insights

| Dimension | Attacker Perspective | Defender Perspective |
| :--- | :--- | :--- |
| **Registrar & Expiration** | Finds expired domains for hijacking and typosquatting lures. | Enforces auto-renewals, registry locks, and WHOIS privacy shields. |
| **DNS & Host Routing** | Uncovers origin IPs behind CDNs to bypass WAF barriers. | Uses Authenticated Origin Pulls and strict security rules. |
| **Geolocation & ASN** | Identifies geographic locations to craft localized pretexting lures. | Enforces geo-blocking and network segmentation. |

---

## 🏛️ Internship Program Attribution
This tool was engineered for **Day 1** of the **Alpha 2 Internship — Cybersecurity Track** organized by **Sqrock IT Solution**.

---

## ⚖️ Legal & Ethical Policy
All intelligence gathering performed by this tool is strictly **passive** using public WHOIS and DNS records. It does not perform invasive port scans, exploitation, or intrusive network requests.
