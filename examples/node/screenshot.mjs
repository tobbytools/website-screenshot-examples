// Bulk full-page screenshots with the Apify client, then download every image.
// Usage: npm install && APIFY_TOKEN=... node screenshot.mjs https://example.com https://www.wikipedia.org
import { ApifyClient } from 'apify-client';
import fs from 'node:fs/promises';

const urls = process.argv.slice(2);
if (!urls.length) urls.push('https://example.com');

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('tobbyb/website-screenshot').call({
    urls,
    devices: ['desktop'],
    formats: ['jpeg'],
    fullPage: true,
});

const { items } = await client.dataset(run.defaultDatasetId).listItems();
await fs.mkdir('screenshots', { recursive: true });
for (const item of items) {
    if (item.status !== 'ok') {
        console.log(`SKIPPED ${item.url}: ${item.errorTitle} (${item.howToFix})`); // errors are not charged
        continue;
    }
    const res = await fetch(item.screenshotUrl);
    const file = `screenshots/${new URL(item.url).hostname}-${item.device}.${item.format === 'jpeg' ? 'jpg' : item.format}`;
    await fs.writeFile(file, Buffer.from(await res.arrayBuffer()));
    console.log(`${file}  ${item.imageWidth}x${item.imageHeight}  complete=${item.fullPageComplete}`);
}
