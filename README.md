<div align="center">

# 🛡️ Sqrock Cybersecurity Internship Program (Alpha 2)
### *Social Engineering Attack Simulations & Defense Using Python*
**Author:** [Md Peer Siddiqui](https://github.com/MdPeerSiddiqui) • **Issuing Body:** Sqrock IT Solution

---

</div>

## 📂 Master Internship Structure

Every single day is isolated into its own dedicated, self-contained folder:

```text
Internship Sqrock/
│
├── 📁 Day01_OSINT_Scanner/             # 🛰️ DAY 1: PEER'S OSINT Scanner Tool
│   ├── peers_scanner.py                # Main passive reconnaissance tool
│   ├── README.md                       # Day 1 guide & documentation
│   ├── requirements.txt                # Day 1 dependencies
│   ├── LICENSE                         # MIT License
│   ├── reports/                        # Day 1 generated JSON scan logs
│   └── screenshots/                    # Day 1 terminal execution proof
│
├── 📁 Day02_Email_Harvesting/          # 📧 DAY 2: Email Harvester & Pretexting Tool
│   ├── email_harvester.py              # Main regex harvester & threat engine
│   ├── lab_target.html                 # Practice company target (Apex Dynamics)
│   ├── README.md                       # Day 2 guide & documentation
│   ├── requirements.txt                # Day 2 dependencies
│   ├── LICENSE                         # MIT License
│   └── reports/                        # Day 2 generated JSON reports
│
├── 📁 reports/                         # 📊 Central Official PDF & Markdown Submissions
│   ├── Day01/                          # Day 1 Official PDF & Markdown Reports
│   │   ├── Day01_OSINT_Report_Sqrock_MdPeerSiddiqui.pdf
│   │   └── day01_osint_report.md
│   └── Day02/                          # Day 2 Official PDF & Markdown Reports
│       ├── Day02_Email_Harvesting_Report_Sqrock_MdPeerSiddiqui.pdf
│       └── day02_email_harvesting_report.md
│
├── 📁 screenshots/                     # 📸 Visual Evidence Organized by Day
│   ├── Day01/                          # Day 1 Terminal Screenshots & Kali Guide
│   └── Day02/                          # Day 2 Terminal Screenshots
│
├── 📁 scripts/                         # ⚙️ Executive PDF Generators
│   ├── generate_day01_pdf.py           # Compiles Day 1 PDF report
│   └── generate_day02_pdf.py           # Compiles Day 2 PDF report
│
├── 📁 docs/                            # 📜 Internship Reference & Notes
│
└── 📜 Sqrock_Cybersecurity_Internship_phase1.pdf  # Official 15-Day Curriculum
```

---

## ⚡ Quick Navigation

| Day | Topic | Tool Folder | Official Deliverable |
|:---:|:---|:---|:---|
| **01** | Passive OSINT & Domain Intelligence | [`Day01_OSINT_Scanner/`](Day01_OSINT_Scanner/) | [`reports/Day01/`](reports/Day01/) |
| **02** | Email Harvesting & Pretexting Threat Analysis | [`Day02_Email_Harvesting/`](Day02_Email_Harvesting/) | [`reports/Day02/`](reports/Day02/) |
| **03** | Phishing URL Anatomy & Detection | *Coming next* | *Pending* |

---

## 🚀 How to Run Any Day's Tool

### Run Day 1:
```powershell
cd Day01_OSINT_Scanner
python peers_scanner.py example.com
```

### Run Day 2:
```powershell
cd Day02_Email_Harvesting
python email_harvester.py --demo
```

---

## ⚖️ Ethical & Legal Compliance Notice
All tools in this repository are developed strictly for **educational, defensive, and authorized research purposes** within controlled lab environments under the **Sqrock IT Solution Cybersecurity Internship Track**.
