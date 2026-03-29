/**
 * Export a poster HTML file to PNG using Puppeteer.
 * Run: npm install puppeteer && node export-node.js ../sample/samplePoster.html
 */

const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

function resolvePaths() {
  const inputArg = process.argv[2] || '../sample/samplePoster.html';
  const outputArg = process.argv[3];
  const inputPath = path.resolve(__dirname, inputArg);
  const outputPath =
    outputArg
      ? path.resolve(__dirname, outputArg)
      : path.join(path.dirname(inputPath), `${path.basename(inputPath, '.html')}.png`);

  return { inputPath, outputPath };
}

async function main() {
  const { inputPath, outputPath } = resolvePaths();
  const html = fs.readFileSync(inputPath, 'utf8');

  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  await page.setViewport({ width: 900, height: 1300, deviceScaleFactor: 2 });
  await page.setContent(html, { waitUntil: 'networkidle0' });

  const el = await page.$('.poster');
  if (!el) {
    throw new Error(`Could not find .poster element in ${inputPath}`);
  }

  await el.screenshot({ path: outputPath });
  await browser.close();
  console.log('Saved:', outputPath);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
