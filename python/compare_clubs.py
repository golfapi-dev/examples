"""Compare two clubs side by side by id or slug.

    python compare_clubs.py drivers <first-slug> <second-slug>

Find slugs with list_drivers.py or search_clubs.py.
"""
import sys

from golfapi import get

if len(sys.argv) != 4:
    sys.exit(__doc__)
club_type, first, second = sys.argv[1:]
a, _ = get(f"/{club_type}/{first}")
b, _ = get(f"/{club_type}/{second}")


def show(club, field):
    value = club.get(field)
    if value is None:
        return "not published"
    if isinstance(value, list):
        return ", ".join(f"{x:g}" if isinstance(x, float) else str(x) for x in value)
    return str(value)


print(f"{'':<18} {a['name']:<28} {b['name']:<28}")
for label, field in [("Maker", None), ("Released", "released"), ("Lofts", "lofts_deg"), ("Hands", "hands"),
                     ("Head volume (cc)", "volume_cc"), ("Adjustable hosel", "adjustable_hosel")]:
    if field is None:
        print(f"{label:<18} {a['manufacturer']['name']:<28} {b['manufacturer']['name']:<28}")
    else:
        print(f"{label:<18} {show(a, field):<28} {show(b, field):<28}")
