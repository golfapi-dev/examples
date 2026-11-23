#!/bin/sh
# GolfAPI.dev from the command line. Set GOLFDEV_API_KEY first.
# A free key is at https://console.golfapi.dev/?plan=free

AUTH="Authorization: Bearer $GOLFDEV_API_KEY"

# What this key can read and the catalog release it reads.
curl -s https://api.golfapi.dev/ -H "$AUTH"

# Drivers released in 2025, 20 per page.
curl -s "https://api.golfapi.dev/drivers?release_year=2025" -H "$AUTH"

# Left-handed drivers in 10.5 degrees.
curl -s "https://api.golfapi.dev/drivers?hand=lh&loft=10.5" -H "$AUTH"

# One club by slug.
curl -s "https://api.golfapi.dev/drivers/<slug>" -H "$AUTH"

# Clubs per maker and release year.
curl -s https://api.golfapi.dev/coverage -H "$AUTH"
