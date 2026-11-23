"""List drivers released in a year, with lofts and hands.

    python list_drivers.py 2025
"""
import sys

from golfapi import get

year = int(sys.argv[1]) if len(sys.argv) > 1 else 2025
page, _ = get("/drivers", release_year=year, limit=100)
for club in page["data"]:
    lofts = ", ".join(f"{x:g}" for x in club.get("lofts_deg", []))
    hands = "/".join(club.get("hands", []))
    print(f"{club['manufacturer']['name']:<12} {club['name']:<32} lofts {lofts or '-':<20} {hands}")
print(f"\n{len(page['data'])} drivers")
