// List drivers released in a year, with lofts and hands.
//   node list-drivers.mjs 2025
import {get} from './golfapi.mjs';

const year = Number(process.argv[2] ?? 2025);
const {body} = await get('/drivers', {release_year: year, limit: 100});
for (const club of body.data) {
  const lofts = (club.lofts_deg ?? []).join(', ') || '-';
  console.log(`${club.manufacturer.name.padEnd(12)} ${club.name.padEnd(32)} lofts ${lofts.padEnd(20)} ${(club.hands ?? []).join('/')}`);
}
console.log(`\n${body.data.length} drivers`);
