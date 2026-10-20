"""
=============================================================================
Sqrock IT Solution — Alpha 2 Cybersecurity Internship
Master CLI Toolkit: Social Engineering Attack & Defense Suite
=============================================================================
Usage:
    python main.py                       # Interactive launcher menu
    python main.py osint google.com      # Run Day 1 directly
=============================================================================
"""

import sys
import os

BANNER = r"""
  ____   ___  ____  ___   ____ _  __   ____  _____ 
 / ___| / _ \|  _ \|  _ \ / ___| |/ /  / ___|| ____|
 \___ \| | | | |_) | |_) | |   | ' /   \___ \|  _|  
  ___) | |_| |  __/|  _ <| |___| . \    ___) | |___ 
 |____/ \__\_\\_|   |_| \_\\____|_|\_\  |____/|_____|
  Cybersecurity Social Engineering Simulation Suite
  Sqrock IT Solution — Alpha 2 Internship Track
"""


def show_menu():
    print(BANNER)
    print("=" * 65)
    print(" [01] Day 1 : Passive OSINT & Domain Intelligence Tool")
    print(" [02] Day 2 : Email Scraper & Pretexting Prep (Coming soon)")
    print(" [03] Day 3 : Phishing URL Risk Scorer (Coming soon)")
    print(" [04] Day 4 : Vishing & Smishing Script Generator (Coming soon)")
    print(" [05] Day 5 : Target Profiler Tool (Coming soon)")
    print(" [06] Day 6 : Spear Phishing Engine (Coming soon)")
    print(" [07] Day 7 : Credential Brute-Force & Rate Limiter (Coming soon)")
    print(" [08] Day 8 : USB Drop Payload Simulator (Coming soon)")
    print(" [09] Day 9 : Fake Social Profile Scorer (Coming soon)")
    print(" [10] Day 10: Honeypot Bait Link Tracker (Coming soon)")
    print(" [11] Day 11: Security Awareness CLI Quiz (Coming soon)")
    print(" [12] Day 12: ML Phishing Email Classifier (Coming soon)")
    print(" [13] Day 13: SIEM Log Anomaly Parser (Coming soon)")
    print(" [14] Day 14: Automated Incident Response Script (Coming soon)")
    print(" [15] Day 15: Full Attack Chain Simulator (Capstone)")
    print(" [00] Exit")
    print("=" * 65)


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command in ("osint", "day1", "day01"):
            target = sys.argv[2] if len(sys.argv) > 2 else "example.com"
            from modules.day01_osint.osint_scanner import run_osint_scan
            run_osint_scan(target)
            return

    while True:
        show_menu()
        try:
            choice = input("\nSelect a tool to launch [0-15]: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting toolkit. Stay safe!")
            break

        if choice in ("0", "00", "exit", "q"):
            print("\nExiting toolkit. Stay safe!")
            break
        elif choice in ("1", "01"):
            from modules.day01_osint.osint_scanner import main as day01_main
            # Clear argv so argparse uses interactive prompt
            sys.argv = [sys.argv[0]]
            day01_main()
            input("\n[Press Enter to return to main menu...]")
        else:
            print(f"\n[!] Module {choice} is in development or not yet implemented.")
            input("\n[Press Enter to return to main menu...]")


if __name__ == "__main__":
    main()
