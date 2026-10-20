"""
Day 01: Passive OSINT & Domain Intelligence
Part of PEER'S OSINT Scanner Suite
Developed for Sqrock IT Solution — Alpha 2 Cybersecurity Internship
"""

import sys
import os

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from peers_scanner import run_peers_scan, main

if __name__ == "__main__":
    main()
