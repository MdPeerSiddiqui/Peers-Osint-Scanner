# 💼 LinkedIn Showcase & Proof of Work Guide

How to document and publish your 15-day Sqrock Cybersecurity Internship on LinkedIn so recruiters and cybersecurity managers see genuine hands-on technical competence.

---

## 📸 1. Capturing Practical Proof (Screenshots)

Recruiters look for proof that **you ran the code yourself**:
1. **Terminal Output**: Run the script in your terminal and take a clean screenshot using **`Windows Key + Shift + S`**.
2. **Code Snippet**: Show the key logic (e.g. `socket.gethostbyname()`, `whois.whois()`).
3. **Save your screenshots**: Save them in the `screenshots/` directory (e.g., `screenshots/day01_terminal.png`) so you can link them in your GitHub README and Markdown reports.

---

## 📝 2. Winning Post Structure for Each Day

Every strong cybersecurity post on LinkedIn follows this 4-step framework:

1. **Catchy Hook**: What did you build today?
2. **The Security Problem**: Why does this matter in real-world attacks/defense?
3. **Technical Execution**: What Python tools/libraries were used?
4. **Attacker vs. Defender Insight**: Why defense matters and how organizations protect against it.
5. **Tags & GitHub Link**: Link to your repo so people can see your clean commits.

---

## 🎯 3. Ready-to-Use LinkedIn Template (Day 1)

```text
🚀 Day 1 of my 15-Day Cybersecurity Internship with Sqrock IT Solution!

Today’s focus: Passive Reconnaissance & OSINT using Python 🐍🔍

Before any social engineering or cyber attack occurs, adversaries perform extensive reconnaissance to profile their target without triggering security alarms. Today, I built an automated OSINT tool in Python that extracts vital domain intelligence passively.

🛠️ What the tool does:
• DNS Resolution: Resolves target domain to IP address using Python's socket library.
• WHOIS Extraction: Identifies domain registrar, creation date, and expiration window.
• IP Geolocation: Maps hosting server coordinates and ISP provider via IP-API.

🛡️ Attacker vs. Defender Perspective:
• Attacker View: Identifying registrar and CDN/hosting providers reveals renewal windows and external infrastructure dependencies.
• Defender View: Security teams must monitor WHOIS privacy, audit exposed DNS records, and watch for typosquatting domains.

📌 Deliverables completed:
- Functional Python OSINT script
- 1-page technical reconnaissance report
- Execution logs verified on lab domain (example.com)

👉 All activities conducted strictly within authorized educational lab environments adhering to IT Act 2000 & CFAA guidelines.

#Cybersecurity #Python #OSINT #InfoSec #Internship #Sqrock #SocialEngineering #EthicalHacking #BlueTeam #Reconnaissance
```
