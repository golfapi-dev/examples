// Search one club type by hand and loft.
//   node search-clubs.mjs drivers lh 10.5
// A loft the collection does not sell returns 400 with the lofts it does sell.
import {get} from './golfapi.mjs';

const [type, hand, loft] = process.argv.slice(2);
if (!loft) throw new Error('Usage: node search-clubs.mjs <club-type> <rh|lh> <loft>');
try {
  const {body} = await get(`/${type}`, {hand, loft, limit: 100});
  for (const club of body.data) console.log(`${club.manufacturer.name.padEnd(12)} ${club.name.padEnd(32)} ${club.slug}`);
  console.log(`\n${body.data.length} ${type} in ${loft} degrees, ${hand}`);
} catch (err) {
  console.error(err.message);
  process.exitCode = 1;
}
