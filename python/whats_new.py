"""Show what changed in the catalog since a release you stored.

    python whats_new.py            # prints the current release id to store
    python whats_new.py bld_...    # lists changes after that release
"""
import sys

from golfapi import get

_, headers = get("/drivers", limit=1)
current = headers.get("Golfapi-Catalog-Release")
if len(sys.argv) < 2:
    print(f"Current catalog release: {current}\nStore it, then run: python whats_new.py {current}")
    sys.exit()
changes, _ = get("/changes", after=sys.argv[1])
releases = changes.get("data", [])
if not releases:
    print("No changes since that release.")
for release in releases:
    print(release["release"], release["published_at"])
    for resource, groups in release.get("changes", {}).items():
        for action in ("added", "updated", "removed"):
            ids = groups.get(action, [])
            if ids:
                print(f"  {resource:<14} {action:<8} {len(ids)} clubs: {', '.join(ids[:5])}{' ...' if len(ids) > 5 else ''}")
