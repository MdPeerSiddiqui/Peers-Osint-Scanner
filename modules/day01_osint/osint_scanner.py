"""
=============================================================================
Sqrock IT Solution — Alpha 2 Cybersecurity Internship
Module: Day 01 - OSINT & Passive Reconnaissance Tool
File: osint_scanner.py
=============================================================================
Usage:
    python osint_scanner.py google.com
    python osint_scanner.py --domain example.com --save
=============================================================================
"""

import argparse
import io
import json
import os
import re
import socket
import sys
from datetime import datetime
import requests
import whois

# Ensure cross-platform UTF-8 terminal printing
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

BANNER = """
===============================================================================
  ____   ____  ___ _   _ _____   ____                                         
 / ___| / ___|/ _ \\ \\ | |_   _| / ___|  ___ __ _ _ __  _ __   ___ _ __        
 \\___ \\| |   | | | |  \\| | | |   \\___ \\ / __/ _` | '_ \\| '_ \\ / _ \\ '__|       
  ___) | |___| |_| | |\\  | | |    ___) | (_| (_| | | | | | | |  __/ |          
 |____/ \\____|\\___/|_| \\_| |_|   |____/ \\___\\__,_|_| |_|_| |_|\\___|_|          
               Day 01: Passive OSINT & Domain Intelligence Tool                
===============================================================================
"""


def clean_domain(domain_input: str) -> str:
    """Strip protocol (http/https) and paths to extract pure domain name."""
    domain = domain_input.strip()
    domain = re.sub(r"^https?://", "", domain, flags=re.IGNORECASE)
    domain = domain.split("/")[0].split(":")[0]
    return domain


def run_osint_scan(domain: str, save_report: bool = True, output_dir: str = "reports") -> dict:
    """
    Perform passive reconnaissance on a given domain.
    Gathers WHOIS registrar details, resolved IP address, and IP geolocation.
    """
    domain = clean_domain(domain)
    print(BANNER)
    print(f"[*] Target Domain       : {domain}")
    print(f"[*] Timestamp           : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 79)

    results = {
        "target_domain": domain,
        "timestamp": datetime.now().isoformat(),
        "dns": {},
        "whois": {},
        "geolocation": {},
    }

    # 1. DNS Resolution
    print("\n[+] 1. RESOLVING DNS...")
    try:
        ip = socket.gethostbyname(domain)
        results["dns"]["ip_address"] = ip
        print(f"    [+] Resolved IP Address : {ip}")
    except socket.gaierror as e:
        print(f"    [-] DNS Resolution Failed: {e}")
        results["dns"]["error"] = str(e)
        return results

    # 2. WHOIS Information
    print("\n[+] 2. QUERYING WHOIS REGISTRY...")
    try:
        w = whois.whois(domain)
        # Normalize list vs single date
        creation = w.creation_date[0] if isinstance(w.creation_date, list) else w.creation_date
        expiration = w.expiration_date[0] if isinstance(w.expiration_date, list) else w.expiration_date

        results["whois"]["registrar"] = w.registrar
        results["whois"]["creation_date"] = str(creation)
        results["whois"]["expiration_date"] = str(expiration)
        results["whois"]["name_servers"] = w.name_servers if w.name_servers else []

        print(f"    |-- Registrar           : {w.registrar or 'N/A'}")
        print(f"    |-- Creation Date       : {creation}")
        print(f"    \\-- Expiration Date     : {expiration}")
    except Exception as e:
        print(f"    \\-- [-] WHOIS Lookup Notice: {e}")
        results["whois"]["error"] = str(e)

    # 3. IP Geolocation (via ip-api)
    print("\n[+] 3. FETCHING GEOLOCATION & NETWORK METRICS...")
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        if resp.status_code == 200:
            geo_data = resp.json()
            if geo_data.get("status") == "success":
                results["geolocation"]["country"] = geo_data.get("country")
                results["geolocation"]["country_code"] = geo_data.get("countryCode")
                results["geolocation"]["region"] = geo_data.get("regionName")
                results["geolocation"]["city"] = geo_data.get("city")
                results["geolocation"]["isp"] = geo_data.get("isp")
                results["geolocation"]["org"] = geo_data.get("org")
                results["geolocation"]["as"] = geo_data.get("as")

                print(f"    |-- Country             : {geo_data.get('country')} ({geo_data.get('countryCode')})")
                print(f"    |-- Region / City       : {geo_data.get('regionName')}, {geo_data.get('city')}")
                print(f"    |-- ISP                 : {geo_data.get('isp')}")
                print(f"    \\-- AS Organization     : {geo_data.get('as')}")
            else:
                print(f"    \\-- [-] Geolocation Query Failed: {geo_data.get('message')}")
        else:
            print(f"    \\-- [-] Geolocation API HTTP Error: {resp.status_code}")
    except Exception as e:
        print(f"    \\-- [-] Geolocation Request Error: {e}")
        results["geolocation"]["error"] = str(e)

    print("\n" + "=" * 79)
    print("                      SCAN EXECUTION COMPLETED")
    print("=" * 79)

    # Save output if requested
    if save_report:
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"osint_{domain}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
        print(f"\n[+] Practical Report Saved: {filename}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Day 1 OSINT Scanner — Passive Reconnaissance Tool (Sqrock IT Solution)"
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=None,
        help="Target domain to scan (e.g., google.com, example.com)",
    )
    parser.add_argument(
        "--domain",
        "-d",
        dest="flag_domain",
        help="Domain option (alternative to positional argument)",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Disable automatic saving of report to reports/",
    )

    args = parser.parse_args()
    domain = args.target or args.flag_domain

    if not domain:
        print(BANNER)
        try:
            domain = input("[?] Enter target domain to scan (e.g., google.com): ").strip()
        except EOFError:
            domain = "google.com"

        if not domain:
            print("[!] Error: No domain provided. Exiting.")
            sys.exit(1)

    run_osint_scan(domain, save_report=not args.no_save)


if __name__ == "__main__":
    main()
