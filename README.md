<img src="https://raw.githubusercontent.com/golfapi-dev/mcp/main/assets/birdie.png" alt="Birdie, the GolfAPI.dev mascot" width="72" align="right" />

# GolfAPI.dev examples

Small scripts that read the GolfAPI.dev catalog. Each one runs on a free key with no dependencies.

1. Get a free key at [console.golfapi.dev](https://console.golfapi.dev/?plan=free&ref=github).
2. Set it in your shell:

```sh
export GOLFDEV_API_KEY='sk_live_...'
```

A free key reads a fixed sample: 20 drivers from 10 makers released in 2025, 2 mini-drivers and 2 fairway woods. The same scripts read the full catalog on a paid plan.

## Python (3.9+)

| Script | What it does |
| --- | --- |
| `python3 list_drivers.py 2025` | Drivers released in a year, with lofts and hands |
| `python3 search_clubs.py drivers lh 10.5` | Clubs of one type in a hand and loft |
| `python3 compare_clubs.py drivers <slug-a> <slug-b>` | Two clubs side by side |
| `python3 whats_new.py [bld_...]` | The current catalog release, or the changes after one you already read |

## JavaScript (Node 18+)

| Script | What it does |
| --- | --- |
| `node list-drivers.mjs 2025` | Drivers released in a year, with lofts and hands |
| `node search-clubs.mjs drivers lh 10.5` | Clubs of one type in a hand and loft |

## curl

[`curl/examples.sh`](curl/examples.sh) lists the same calls as plain requests.

## Reference

- API reference: [golfapi.dev/docs](https://golfapi.dev/docs/?ref=github)
- OpenAPI description: [golfapi-dev/openapi](https://github.com/golfapi-dev/openapi)
- MCP server for AI assistants: [golfapi-dev/mcp](https://github.com/golfapi-dev/mcp)

## License

The code in this repository is MIT licensed. Catalog data read through the API is covered by the [GolfAPI.dev Terms](https://golfapi.dev/terms/).
