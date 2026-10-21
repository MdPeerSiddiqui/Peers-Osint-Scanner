r"""
================================================================================
  ____  _____ _____ ____  _ ____     ___  ____ ___ _   _ _____ 
 |  _ \| ____| ____|  _ \/ / ___|   / _ \/ ___|_ _| \ | |_   _|
 | |_) |  _| |  _| | |_) | \___ \  | | | \___ \| ||  \| | | |  
 |  __/| |___| |___|  _ <   ___) | | |_| |___) | || |\  | | |  
 |_|   |_____|_____|_| \_\ |____/   \___/|____/___|_| \_| |_|  
  ____   ____    _    _   _ _   _ _____ ____                 
 / ___| / ___|  / \  | \ | | \ | | ____|  _ \                
 \___ \| |     / _ \ |  \| |  \| |  _| | |_) |               
  ___) | |___ / ___ \| |\  | |\  | |___|  _ <                
 |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\               
                                                             
  ⚡ PEER'S OSINT SCANNER — Advanced Passive Reconnaissance Tool ⚡
  Developed under Sqrock IT Solution — Alpha 2 Cybersecurity Internship
================================================================================
"""

import argparse
import ipaddress
import json
import os
import re
import socket
import sys
from datetime import datetime
import requests
import whois

# Cross-platform color styling with graceful fallback
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    C_CYAN = Fore.CYAN
    C_GREEN = Fore.GREEN
    C_YELLOW = Fore.YELLOW
    C_RED = Fore.RED
    C_MAGENTA = Fore.MAGENTA
    C_WHITE = Fore.WHITE
    C_BRIGHT = Style.BRIGHT
    C_DIM = Style.DIM
    C_RESET = Style.RESET_ALL
except ImportError:
    C_CYAN = "\033[36m"
    C_GREEN = "\033[32m"
    C_YELLOW = "\033[33m"
    C_RED = "\033[31m"
    C_MAGENTA = "\033[35m"
    C_WHITE = "\033[37m"
    C_BRIGHT = "\033[1m"
    C_DIM = "\033[2m"
    C_RESET = "\033[0m"

# Ensure UTF-8 printing in Windows terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

BANNER = rf"""{C_CYAN}{C_BRIGHT}
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
{C_RESET}
{C_YELLOW}{C_BRIGHT} ⚡ PEER'S OSINT SCANNER v1.0 — Passive Reconnaissance Suite ⚡{C_RESET}
{C_WHITE}{C_DIM} [★] Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Internship{C_RESET}
{C_CYAN}{"=" * 75}{C_RESET}
"""


def clean_target(target_input: str) -> str:
    """Clean protocol prefix, trailing slashes, and ports."""
    target = target_input.strip()
    target = re.sub(r"^https?://", "", target, flags=re.IGNORECASE)
    target = target.split("/")[0].split(":")[0]
    return target


def is_ip_address(target: str) -> bool:
    """Check if target string is a valid IPv4 or IPv6 address."""
    try:
        ipaddress.ip_address(target)
        return True
    except ValueError:
        return False


def run_peers_scan(target: str, save_report: bool = True, output_dir: str = "reports") -> dict:
    """Execute complete PEER'S OSINT Scan on target domain or IP."""
    target = clean_target(target)
    is_ip = is_ip_address(target)
    scan_time = datetime.now()

    print(f"\n{C_GREEN}{C_BRIGHT}[*] TARGET IDENTIFIED :{C_RESET} {C_WHITE}{C_BRIGHT}{target}{C_RESET}")
    print(f"{C_GREEN}[*] TARGET TYPE       :{C_RESET} {'IPv4/IPv6 Address' if is_ip else 'Domain Name'}")
    print(f"{C_GREEN}[*] TIME OF SCAN      :{C_RESET} {scan_time.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{C_CYAN}{'-' * 75}{C_RESET}")

    report = {
        "tool": "PEER'S OSINT Scanner",
        "program": "Sqrock IT Solution — Alpha 2 Cybersecurity Internship",
        "target": target,
        "target_type": "IP" if is_ip else "Domain",
        "timestamp": scan_time.isoformat(),
        "dns": {},
        "whois": {},
        "geolocation": {},
        "threat_intel": {}
    }

    # -------------------------------------------------------------
    # STEP 1: DNS & IP Resolution
    # -------------------------------------------------------------
    print(f"\n{C_YELLOW}{C_BRIGHT}[1] RESOLVING DNS & HOST ROUTING...{C_RESET}")
    if is_ip:
        ip = target
        report["dns"]["ip_address"] = ip
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            report["dns"]["reverse_hostname"] = hostname
            print(f"    {C_GREEN}[+] IP Address       :{C_RESET} {ip}")
            print(f"    {C_GREEN}[+] Reverse Hostname :{C_RESET} {hostname}")
        except Exception as e:
            report["dns"]["reverse_hostname"] = "None (No PTR record)"
            print(f"    {C_GREEN}[+] IP Address       :{C_RESET} {ip}")
            print(f"    {C_WHITE}{C_DIM}[~] Reverse Hostname :{C_RESET} No PTR record found ({e})")
    else:
        domain = target
        try:
            ip = socket.gethostbyname(domain)
            report["dns"]["domain"] = domain
            report["dns"]["ip_address"] = ip
            print(f"    {C_GREEN}[+] Target Domain    :{C_RESET} {domain}")
            print(f"    {C_GREEN}[+] Resolved IPv4    :{C_RESET} {ip}")
        except socket.gaierror as e:
            print(f"    {C_RED}[!] DNS Resolution Error: Could not resolve '{domain}' ({e}){C_RESET}")
            report["dns"]["error"] = str(e)
            return report

    # -------------------------------------------------------------
    # STEP 2: WHOIS Registry Information
    # -------------------------------------------------------------
    print(f"\n{C_YELLOW}{C_BRIGHT}[2] QUERYING WHOIS REGISTRATION INTELLIGENCE...{C_RESET}")
    lookup_target = target if not is_ip else ip
    try:
        w = whois.whois(lookup_target)
        creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
        expiration = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date

        report["whois"]["registrar"] = w.registrar or "N/A"
        report["whois"]["creation_date"] = str(creation)
        report["whois"]["expiration_date"] = str(expiration)
        report["whois"]["name_servers"] = w.name_servers if w.name_servers else []

        print(f"    {C_GREEN}[+] Registrar        :{C_RESET} {w.registrar or 'N/A'}")
        print(f"    {C_GREEN}[+] Registered Date  :{C_RESET} {creation}")
        print(f"    {C_GREEN}[+] Expiration Date  :{C_RESET} {expiration}")
        if w.name_servers:
            ns_list = w.name_servers if isinstance(w.name_servers, list) else [w.name_servers]
            print(f"    {C_GREEN}[+] Name Servers     :{C_RESET} {', '.join([str(n) for n in ns_list[:3]])}")
    except Exception as e:
        print(f"    {C_WHITE}{C_DIM}[~] WHOIS Registry   : Query note - {e}{C_RESET}")
        report["whois"]["notice"] = str(e)

    # -------------------------------------------------------------
    # STEP 3: IP Geolocation & ASN Details
    # -------------------------------------------------------------
    print(f"\n{C_YELLOW}{C_BRIGHT}[3] GEOLOCATION, ASN & INFRASTRUCTURE DATA...{C_RESET}")
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,regionName,city,zip,lat,lon,timezone,isp,org,as,query", timeout=10)
        if resp.status_code == 200:
            geo = resp.json()
            if geo.get("status") == "success":
                report["geolocation"] = {
                    "country": geo.get("country"),
                    "country_code": geo.get("countryCode"),
                    "region": geo.get("regionName"),
                    "city": geo.get("city"),
                    "coordinates": f"{geo.get('lat')}, {geo.get('lon')}",
                    "timezone": geo.get("timezone"),
                    "isp": geo.get("isp"),
                    "organization": geo.get("org"),
                    "asn": geo.get("as")
                }
                print(f"    {C_GREEN}[+] Country          :{C_RESET} {geo.get('country')} ({geo.get('countryCode')})")
                print(f"    {C_GREEN}[+] City / Region    :{C_RESET} {geo.get('city')}, {geo.get('regionName')}")
                print(f"    {C_GREEN}[+] Coordinates      :{C_RESET} {geo.get('lat')}, {geo.get('lon')}")
                print(f"    {C_GREEN}[+] ISP Provider     :{C_RESET} {geo.get('isp')}")
                print(f"    {C_GREEN}[+] Organization     :{C_RESET} {geo.get('org')}")
                print(f"    {C_GREEN}[+] AS Number        :{C_RESET} {geo.get('as')}")

                # Passive threat indicators
                isp_lower = (geo.get("isp") or "").lower()
                org_lower = (geo.get("org") or "").lower()
                if "cloudflare" in isp_lower or "cloudflare" in org_lower:
                    report["threat_intel"]["cdn"] = "Cloudflare Reverse Proxy Detected"
                    print(f"    {C_CYAN}[i] Security Posture :{C_RESET} Cloudflare WAF / Reverse Proxy Protection")
                elif "amazon" in org_lower or "aws" in isp_lower:
                    report["threat_intel"]["cloud"] = "Amazon Web Services (AWS)"
                    print(f"    {C_CYAN}[i] Cloud Provider   :{C_RESET} Amazon Web Services (AWS)")
                elif "google" in org_lower or "google" in isp_lower:
                    report["threat_intel"]["cloud"] = "Google Cloud Infrastructure"
                    print(f"    {C_CYAN}[i] Cloud Provider   :{C_RESET} Google Cloud Infrastructure")
            else:
                print(f"    {C_RED}[!] Geolocation Query Failed: {geo.get('message')}{C_RESET}")
        else:
            print(f"    {C_RED}[!] Geolocation HTTP Error: {resp.status_code}{C_RESET}")
    except Exception as e:
        print(f"    {C_RED}[!] Geolocation Request Error: {e}{C_RESET}")
        report["geolocation"]["error"] = str(e)

    # -------------------------------------------------------------
    # SUMMARY CARD
    # -------------------------------------------------------------
    print(f"\n{C_CYAN}{'=' * 75}{C_RESET}")
    print(f"{C_GREEN}{C_BRIGHT}                      ✔ SCAN COMPLETED SUCCESSFULLY{C_RESET}")
    print(f"{C_CYAN}{'=' * 75}{C_RESET}")

    safe_name = re.sub(r"[^a-zA-Z0-9.-]", "_", target)
    if save_report:
        os.makedirs(output_dir, exist_ok=True)
        json_path = os.path.join(output_dir, f"peers_scan_{safe_name}.json")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4)
        print(f"\n{C_WHITE}[★] Structured JSON Report Saved  : {C_GREEN}{json_path}{C_RESET}")

    return report


def main():
    print(BANNER)
    parser = argparse.ArgumentParser(
        description="PEER'S OSINT Scanner — Developed for Sqrock IT Solution Cybersecurity Track"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="Target domain or IPv4/IPv6 address (e.g., google.com or 8.8.8.8)",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Do not save the JSON report to the reports folder",
    )

    args = parser.parse_args()
    target = args.target

    # If no target passed as argument, interactively ask the user
    if not target:
        try:
            print(f"{C_YELLOW}[?] Enter Target Domain or IP Address (e.g. example.com){C_RESET}")
            target = input(f"{C_CYAN}    └── Target > {C_RESET}").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C_RED}[!] Scan aborted by user.{C_RESET}")
            sys.exit(0)

    if not target:
        print(f"{C_RED}[!] Error: No domain or IP entered. Exiting.{C_RESET}")
        sys.exit(1)

    run_peers_scan(target, save_report=not args.no_save)


if __name__ == "__main__":
    main()
