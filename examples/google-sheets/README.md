# Screenshots inside Google Sheets

Every successful row in the dataset has a `sheetsImageFormula` column such as
`=IMAGE("https://api.apify.com/v2/key-value-stores/…/records/example-com-desktop-….jpg?signature=…")`.

1. Run the Actor in the Apify Console with your URLs.
2. Open the run's **Output** tab and pick the **Sheets** view (flat table).
3. Export as CSV (or use Apify's Google Sheets integration) and import it into a sheet.
4. The `sheetsImageFormula` cells render the screenshot thumbnails. The image links are signed and keep working.

Tip: for a recurring report, create an Apify Schedule for the Actor and connect the
[Google Sheets integration](https://docs.apify.com/platform/integrations) so each run appends new rows.
