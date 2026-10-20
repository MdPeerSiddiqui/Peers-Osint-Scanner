# 🛡️ Sqrock CyberSec Toolkit — Social Engineering Simulation Suite
> **Alpha 2 Internship — Cybersecurity Track (Phase 1)**  
> **Issuing Body:** Sqrock IT Solution  
> **Core Focus:** Practical Social Engineering Attack & Defense Tools in Python

---

## ⚡ Quick Start (Clone & Run in 30 Seconds)

Anyone can clone and run these tools immediately:

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/social-engineering-toolkit.git
cd social-engineering-toolkit
```

### 2. Set Up Virtual Environment & Install Dependencies
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Tools

#### Option A: Direct Domain Scan (Day 1 OSINT)
Type any domain (e.g., `google.com` or `example.com`):
```bash
python modules/day01_osint/osint_scanner.py google.com
```

#### Option B: Master CLI Launcher
Launch the interactive suite menu or pass commands:
```bash
python main.py osint google.com
```

---

## 📂 Project Structure (Human-Readable & Modular)

The project is structured so anyone looking at the files instantly understands their purpose:

```text
├── main.py                             # 🚀 Central Interactive CLI Launcher
├── requirements.txt                    # 📦 Python dependencies
├── README.md                           # 📖 Project documentation & Quickstart
│
├── modules/                            # 🛠️ Day-by-Day Tools (Modular Python Packages)
│   ├── day01_osint/                    # [Day 01] Passive OSINT & Domain Intelligence
│   ├── day02_email_harvesting/         # [Day 02] Regex Scraper & Pretexting Prep
│   ├── day03_phishing_detector/        # [Day 03] URL Phishing Risk Scorer
│   ├── day04_vishing_smishing/         # [Day 04] Vishing/Smishing Script Engine
│   ├── day05_target_profiling/         # [Day 05] Public Profile Aggregation Tool
│   ├── day06_spear_phishing/           # [Day 06] Spear Phishing Template Generator
│   ├── day07_credential_stuffing/      # [Day 07] Credential Brute-Force & Rate Limiter
│   ├── day08_usb_drop/                 # [Day 08] Benign USB Drop Payload Simulator
│   ├── day09_fake_profile_detector/    # [Day 09] Bot / Impersonation Heuristic Scorer
│   ├── day10_honeypot/                 # [Day 10] Bait Link Honeypot Tracker
│   ├── day11_awareness_quiz/           # [Day 11] Interactive Security Awareness Quiz
│   ├── day12_ml_phishing_detection/    # [Day 12] Naive Bayes ML Phishing Classifier
│   ├── day13_siem_log_analysis/        # [Day 13] SIEM Log Anomaly Parser
│   ├── day14_incident_response/        # [Day 14] Automated Containment & IR Script
│   └── day15_capstone_attack_chain/    # [Day 15] Full Attack Chain Simulator (Unified CLI)
│
├── reports/                            # 📊 Practical Reports, Deliverables & JSON Logs
│   ├── day01_osint_report.md
│   └── osint_google.com.json
│
├── screenshots/                        # 📸 Visual Proof of Execution (For LinkedIn & GitHub)
│
└── docs/                               # 📜 Guidelines & Trackers
    ├── ETHICAL_GUIDELINES.md           # Legal & ethical boundaries
    ├── PROGRESS_TRACKER.md             # 15-day milestone checklist
    └── LINKEDIN_SHOWCASE_GUIDE.md      # How to showcase practical proof on LinkedIn
```

---

## ⚖️ Ethical & Legal Compliance Notice
This repository is developed for **educational, defensive, and authorized awareness training purposes only**. All exercises are executed against authorized lab domains or local test harnesses (`localhost`). Unauthorized scanning, phishing, or testing against third-party systems without prior explicit written permission violates the Indian Information Technology Act (2000), US Computer Fraud and Abuse Act (CFAA), and international cybersecurity laws. See [`docs/ETHICAL_GUIDELINES.md`](docs/ETHICAL_GUIDELINES.md).
