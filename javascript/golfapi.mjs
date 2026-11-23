// Minimal GolfAPI.dev client for Node 18+. No dependencies.
// Set GOLFDEV_API_KEY to your key (a free key is at https://console.golfapi.dev/?plan=free).

const BASE = 'https://api.golfapi.dev';

export async function get(path, params = {}) {
  const key = process.env.GOLFDEV_API_KEY;
  if (!key) throw new Error('Set GOLFDEV_API_KEY first. A free key is at https://console.golfapi.dev/?plan=free');
  const query = new URLSearchParams(Object.entries(params).filter(([, v]) => v != null)).toString();
  const res = await fetch(`${BASE}${path}${query ? `?${query}` : ''}`, {
    headers: {Authorization: `Bearer ${key}`, Accept: 'application/json', 'User-Agent': 'golfapi-examples/1.0'},
  });
  const body = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(`${res.status}: ${body.error?.message ?? res.statusText}`);
  return {body, headers: res.headers};
}
