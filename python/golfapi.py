"""Minimal GolfAPI.dev client. Standard library only.

Set GOLFDEV_API_KEY to your key (a free key is at https://console.golfapi.dev/?plan=free).
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://api.golfapi.dev"


def get(path, **params):
    """GET a path with query parameters. Returns (body, headers)."""
    key = os.environ.get("GOLFDEV_API_KEY")
    if not key:
        sys.exit("Set GOLFDEV_API_KEY first. A free key is at https://console.golfapi.dev/?plan=free")
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{BASE}{path}" + (f"?{query}" if query else "")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
        "User-Agent": "golfapi-examples/1.0",
    })
    try:
        with urllib.request.urlopen(req) as res:
            return json.load(res), res.headers
    except urllib.error.HTTPError as err:
        body = json.load(err) if err.headers.get_content_type() == "application/json" else {}
        message = body.get("error", {}).get("message") or err.reason
        sys.exit(f"{err.code}: {message}")
