"""Search one club type by hand and loft.

    python search_clubs.py drivers lh 10.5

A loft the collection does not sell returns 400 with the lofts it does sell.
"""
import sys

from golfapi import get

if len(sys.argv) != 4:
    sys.exit(__doc__)
club_type, hand, loft = sys.argv[1:]
page, _ = get(f"/{club_type}", hand=hand, loft=loft, limit=100)
for club in page["data"]:
    print(f"{club['manufacturer']['name']:<12} {club['name']:<32} {club['slug']}")
print(f"\n{len(page['data'])} {club_type} in {loft} degrees, {hand}")
