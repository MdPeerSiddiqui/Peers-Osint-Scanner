# 💼 LinkedIn Showcase & Proof of Work Guide

How to document and publish **PEER'S OSINT Scanner** and your 15-day Sqrock Cybersecurity Internship on LinkedIn so recruiters, security engineers, and hiring managers recognize genuine technical craftsmanship.

---

## 📸 1. Capturing Practical Proof (Screenshots)

To show genuine hands-on work:
1. **Terminal Screenshot**:
   - Run:
     ```powershell
     .\.venv\Scripts\python.exe peers_scanner.py example.com
     ```
   - Press **`Windows Key + Shift + S`** to snip the terminal showing the colorful **PEER'S OSINT SCANNER** banner, the resolved `example.com` data, and the success card.
2. **Side-by-Side Code Screenshot**:
   - Split your screen with VS Code on the left showing `peers_scanner.py` and the terminal on the right.
3. **Save to Repo**:
   - Save the image to `screenshots/peers_scanner_demo.png`.

---

## 🎯 2. Ready-to-Publish LinkedIn Post (Day 1)

Copy and paste this directly on LinkedIn:

```text
🚀 Excited to launch PEER'S OSINT Scanner — Day 1 of my Cybersecurity Internship at Sqrock IT Solution! 🛰️🔍

Before an adversary launches a targeted social engineering or cyber attack, they perform passive reconnaissance to gather intelligence without touching the target's internal security perimeter.

To simulate and understand this phase, I built "PEER'S OSINT Scanner", a modular Python-based reconnaissance tool that passively fingerprints domains and IP addresses.

⚡ Key Features:
• Dual-Target Recognition: Dynamically handles both FQDN domains and raw IPv4/IPv6 addresses.
• Forward & Reverse DNS: Automates A record lookup and reverse PTR hostname resolution.
• WHOIS Extraction: Scrapes registry metadata, domain creation/expiration windows, and authoritative Name Servers.
• Geolocation & ASN Mapping: Tracks server geography (Country, Region, City, Coordinates) and identifies ISP & Autonomous System Numbers.
• Passive Threat Fingerprinting: Identifies reverse proxies (Cloudflare WAF) and cloud infrastructure (AWS / GCP).
• Audit Deliverables: Automatically saves structured JSON reports for SOC and threat-intel logs.

🛡️ Attacker vs. Defender Perspective:
• Attacker View: Mapping registrar and renewal windows enables domain hijacking/squatting strategies; ASN details reveal hosting dependencies.
• Defender View: Organizations must enforce WHOIS privacy, audit DNS records against spoofing, and ensure cloud providers deploy hardened WAF configurations.

💻 Open-Source GitHub Repository:
👉 [Insert your GitHub repo link here]

All experiments were conducted strictly within authorized lab environments following ethical hacking standards and IT Act 2000 / CFAA compliance.

Big thanks to Sqrock IT Solution for this hands-on cybersecurity curriculum!

#Cybersecurity #OSINT #Python #InformationSecurity #EthicalHacking #SqrockITSolution #Internship #ThreatIntelligence #BlueTeam #Reconnaissance #Networking
```
