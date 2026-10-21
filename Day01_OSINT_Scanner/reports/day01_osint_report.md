# Day 1 Deliverable: OSINT & Passive Reconnaissance Report

- **Intern Name:** [Your Name]
- **Organization:** Sqrock IT Solution
- **Program:** Alpha 2 Internship — Cybersecurity Track
- **Target Domain:** `example.com`
- **Date:** 2026-10-20

---

## 1. Executive Summary
This exercise demonstrates passive open-source reconnaissance (OSINT). Passive reconnaissance gathers intelligence about a target organization from public sources without directly interacting or sending unsolicited intrusion traffic to their target systems.

---

## 2. Technical Findings

| Field | Gathered Value |
| :--- | :--- |
| **Domain** | `example.com` |
| **Resolved IP** | `172.66.147.243` |
| **Domain Registrar** | RESERVED-Internet Assigned Numbers Authority |
| **Domain Creation Date** | 1995-08-14 |
| **Domain Expiration Date** | 2027-08-13 |
| **Hosting Geolocation** | Toronto, Canada |
| **Hosting Provider / ISP** | Cloudflare, Inc. |

---

## 3. Passive vs. Active Reconnaissance Analysis

* **Passive Reconnaissance**:
  - Gathers intelligence from third-party databases (WHOIS repositories, DNS servers, search engines, Shodan, GitHub leaks).
  - Target system logs show **zero** evidence of your IP address or activity.
* **Active Reconnaissance**:
  - Involves direct interaction with the target (port scanning with Nmap, banner grabbing, web vulnerability scanning).
  - Highly detectable by IDS/IPS and Web Application Firewalls (WAFs).

---

## 4. Attacker vs. Defender Implications

* **Attacker Perspective**:
  - Identifying the registrar and name servers allows attackers to locate third-party suppliers and identify renewal windows (useful for domain hijacking/squatting).
  - IP and ISP info indicates CDN usage (e.g., Cloudflare) or cloud hosting (AWS, GCP), shaping subsequent evasion tactics.
* **Defender Perspective**:
  - Security teams must use WHOIS privacy protections, monitor DNS records for unauthorized changes, and audit what technical metadata is exposed publicly.

---

## 5. Script Output Log

```json
{
  "domain": "example.com",
  "ip": "172.66.147.243",
  "registrar": "RESERVED-Internet Assigned Numbers Authority",
  "creation_date": "1995-08-14 04:00:00+00:00",
  "expiration_date": "2027-08-13 04:00:00+00:00",
  "city": "Toronto",
  "country": "Canada",
  "isp": "Cloudflare, Inc."
}
```
