# karnataka-tenders

Dataset of tenders issued in Karnataka. Sourced from the [Karnataka Public Procurement Portal](https://kppp.karnataka.gov.in).

Browse the latest tenders here: <https://flatgithub.com/Vonter/karnataka-tenders?filename=csv/LatestTenders.csv&stickyColumnName=Tender%20Number&sort=Published%20Date%2Cdesc>.

Browse the entire dataset here: <https://flatgithub.com/Vonter/karnataka-tenders?filename=csv/AllTenders.csv&stickyColumnName=Tender%20Number&sort=Published%20Date%2Cdesc>.

## Scripts

- [fetch.sh](fetch.sh): Fetches the raw JSON data from the [Karnataka Public Procurement Portal](https://kppp.karnataka.gov.in)
- [flatten.py](flatten.py): Parses the raw JSON, and generates the CSV dataset

## License

This karnataka-tenders dataset is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. 
Some individual contents of the database are under copyright by KPPP.

You are free:

* **To share**: To copy, distribute and use the database.
* **To create**: To produce works from the database.
* **To adapt**: To modify, transform and build upon the database.

As long as you:

* **Attribute**: You must attribute any public use of the database, or works produced from the database, in the manner specified in the ODbL. For any use or redistribution of the database, or works produced from it, you must make clear to others the license of the database and keep intact any notices on the original database.
* **Share-Alike**: If you publicly use any adapted version of this database, or works produced from an adapted database, you must also offer that adapted database under the ODbL.
* **Keep open**: If you redistribute the database, or an adapted version of it, then you may use technological measures that restrict the work (such as DRM) as long as you also redistribute a version without such measures.

## Generating

Ensure you have `bash`, `curl` and `python` installed

```
# Fetch the data
bash fetch.sh

# Generate the CSV
python flatten.py
```

The fetch script sources data from Karnataka Public Procurement Portal (https://kppp.karnataka.gov.in)

## TODO

- Automatically fetch latest tenders
- Details from tender documents
- Additional columns for location/area filtering

## Credits

- [Karnataka Public Procurement Portal](https://kppp.karnataka.gov.in)
