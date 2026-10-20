# 🛰️ PEER'S OSINT SCANNER

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue?style=for-the-badge&logo=python" alt="Python Version" />
  <img src="https://img.shields.io/badge/Track-Cybersecurity%20Alpha%202-red?style=for-the-badge&logo=shield" alt="Cybersecurity Track" />
  <img src="https://img.shields.io/badge/Organization-Sqrock%20IT%20Solution-green?style=for-the-badge" alt="Sqrock IT Solution" />
  <img src="https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge" alt="Status" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge" alt="License" />
</p>

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

 ⚡ PEER'S OSINT SCANNER — Advanced Passive Reconnaissance Suite ⚡
 [★] Developed under Sqrock IT Solution — Alpha 2 Cybersecurity Internship
```

**PEER'S OSINT Scanner** is a fast, elegant, and modular passive open-source intelligence (OSINT) tool engineered in Python. It allows cybersecurity analysts, red-teamers, and blue-team defenders to passively fingerprint any **Domain Name** or **IPv4/IPv6 Address** without generating invasive alert traffic on target perimeter firewalls.

---

## ⚡ Highlights & Capabilities

- 🌐 **Dual Target Support**: Automatically detects whether the target is an **FQDN Domain** or an **IPv4/IPv6 Address**.
- 📡 **DNS & Reverse PTR Routing**:
  - Resolves forward A records for domains.
  - Performs reverse DNS PTR lookups for raw IP addresses.
- 📜 **Deep WHOIS Registry Intelligence**:
  - Extracts registrar organization, registered creation date, and expiration window.
  - Lists authoritative primary and secondary Name Servers.
- 🌍 **Geolocation & Infrastructure Profiling**:
  - Maps physical server geolocation: Country, City, Region, Zip, and Geographic Coordinates.
  - Identifies Network Autonomous System Number (ASN), ISP, and parent organization.
- 🛡️ **Passive Security & Cloud Fingerprinting**:
  - Flags reverse proxies and WAF protections (e.g., Cloudflare).
  - Detects major cloud hosting providers (AWS, Google Cloud, Azure).
- 💾 **Automated Security Reports**:
  - Automatically exports structured, audit-ready JSON deliverables to `reports/`.

---

## 🚀 Quickstart Guide (Clone & Run in 10 Seconds)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/peers-osint-scanner.git
cd peers-osint-scanner
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create and activate virtual environment
python -m venv .venv

# On Windows:
.\.venv\Scripts\activate

# On Linux / macOS:
source .venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Launch PEER'S Scanner

#### 🎯 Option A: Interactive Mode (Simply prompts for Domain or IP)
```bash
python peers_scanner.py
```
*The scanner will prompt:*
```text
[?] Enter Target Domain or IP Address
    └── Target > google.com
```

#### ⚡ Option B: Direct Command-line Execution
```bash
# Scan a domain
python peers_scanner.py google.com

# Scan an IP address directly
python peers_scanner.py 8.8.8.8
```

---

## 🖥️ Live Terminal Preview

```text
===========================================================================
[*] TARGET IDENTIFIED : google.com
[*] TARGET TYPE       : Domain Name
[*] TIME OF SCAN      : 2026-10-20 13:24:07 UTC
---------------------------------------------------------------------------

[1] RESOLVING DNS & HOST ROUTING...
    [+] Target Domain    : google.com
    [+] Resolved IPv4    : 142.250.77.142

[2] QUERYING WHOIS REGISTRATION INTELLIGENCE...
    [+] Registrar        : MarkMonitor, Inc.
    [+] Registered Date  : 1997-09-15 04:00:00+00:00
    [+] Expiration Date  : 2028-09-14 04:00:00+00:00
    [+] Name Servers     : NS1.GOOGLE.COM, NS2.GOOGLE.COM, NS3.GOOGLE.COM

[3] GEOLOCATION, ASN & INFRASTRUCTURE DATA...
    [+] Country          : United States (US)
    [+] City / Region    : Mountain View, California
    [+] Coordinates      : 37.4225, -122.085
    [+] ISP Provider     : Google LLC
    [+] Organization     : Google LLC
    [+] AS Number        : AS15169 Google LLC
    [i] Cloud Provider   : Google Cloud Infrastructure

===========================================================================
                      ✔ SCAN COMPLETED SUCCESSFULLY
===========================================================================

[★] Structured JSON Report Saved  : reports/peers_scan_google.com.json
```

---

## 📂 Project Architecture

The directory structure is organized with clean separation of modules, reports, and documentation:

```text
peers-osint-scanner/
├── peers_scanner.py                    # 🚀 Primary PEER'S Scanner CLI Tool
├── main.py                             # 🎛️ Master 15-Day Internship Suite Launcher
├── requirements.txt                    # 📦 Python Dependencies
├── README.md                           # 📖 Project Documentation & Showcase
│
├── modules/                            # 🧩 Modular Subpackages
│   ├── day01_osint/                    # Day 1 OSINT Module (Peer's Scanner Core)
│   ├── day02_email_harvesting/         # Day 2 Email Harvester
│   ├── day03_phishing_detector/        # Day 3 Phishing Risk Scorer
│   └── ...                             # Days 04 to 15
│
├── reports/                            # 📊 Audit-ready JSON Reports & Deliverables
│   ├── day01_osint_report.md           # Formal 1-page internship report
│   ├── peers_scan_google.com.json      # Verified scan result
│   └── peers_scan_8.8.8.8.json         # IP lookup result
│
├── screenshots/                        # 📸 Practical Proof of Execution (Terminal & Code)
│
└── docs/                               # 📜 Professional Documentation
    ├── ETHICAL_GUIDELINES.md           # Legal & ethical boundaries (IT Act 2000 & CFAA)
    ├── PROGRESS_TRACKER.md             # 15-Day Milestone Progress Tracker
    └── LINKEDIN_SHOWCASE_GUIDE.md      # Step-by-step LinkedIn portfolio guide
```

---

## 🛡️ Attacker vs. Defender Security Insights

| Perspective | Security Application |
| :--- | :--- |
| **Attacker (Adversary Profile)** | Identifies domain expiration dates for domain hijacking/squatting, maps external CDN providers to find bypass opportunities, and analyzes geolocation to craft geo-targeted phishing lures. |
| **Defender (Security Team)** | Audits WHOIS privacy disclosure, validates DNS record integrity against spoofing, verifies reverse PTR records, and ensures external cloud providers deploy proper DDoS/WAF safeguards. |

---

## 🏛️ Internship Program Context
This tool was engineered for **Day 1** of the **Alpha 2 Internship — Cybersecurity Track** hosted by **Sqrock IT Solution**.  
* **Curriculum Focus**: Social Engineering Attack Simulations & Defense Using Python (15-Day Calendar).

---

## ⚖️ Legal Disclaimer & Ethics
**FOR AUTHORIZED LAB AND EDUCATIONAL USE ONLY.**  
This tool utilizes publicly available, non-intrusive DNS and WHOIS endpoints. It does not perform invasive port scanning, packet injection, or exploitation. All activities must comply with the Indian Information Technology Act (2000), the United States Computer Fraud and Abuse Act (CFAA), and global data protection standards.
