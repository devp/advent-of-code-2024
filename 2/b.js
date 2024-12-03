const fs = require('fs');

const filename = process.argv[process.argv.length - 1];
const reports = fs.readFileSync(filename).toString().trim().split("\n").map(
  (line) => line.split(" ").map(
    (v) => parseInt(v, 10)
  )
);

const is_safe_report = (r) => {
  if (r.length < 2) { return false; }
  const increasing = r[1] > r[0];
  for (let i = 1; i < r.length; i++) {
    const diff = r[i] - r[i - 1];
    const safe_dir = increasing ? diff > 0 : diff < 0;
    const safe_diff = (Math.abs(diff) <= 3) && (Math.abs(diff) >= 1);
    if (safe_dir && safe_diff) {
      // continue
    } else {
      return false;
    }
  }
  return true;
};

const is_safe_report_with_dampener = (r) => {
  if (is_safe_report(r)) { return true; }
  for (let i = 0; i < r.length; i++) {
    const r2 = Array.from(r);
    r2.splice(i, 1);
    if (is_safe_report(r2)) { return true; }
  }
  return false;
};

const safe_count = reports.filter(is_safe_report_with_dampener).length;

console.log(safe_count);
