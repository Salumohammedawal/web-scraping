# Book Scraper

A Python web scraper that extracts book data from [books.toscrape.com](https://books.toscrape.com) and saves it to a CSV file.

## What it does

- Fetches the homepage of books.toscrape.com
- Parses the HTML using BeautifulSoup
- Extracts the title, price, and availability for every book on the page
- Writes the results to `books.csv`

## How to run it

1. Install the required libraries:

```bash
pip install requests beautifulsoup4 lxml
```

2. Run the script:

```bash
python scraping.py
```

3. Open `books.csv` to see the results.

## Sample output

| title | price | availability |
|-------|-------|--------------|
| A Light in the Attic | £51.77 | In stock |
| Tipping the Velvet | £53.74 | In stock |
| Soumission | £50.10 | In stock |

## Concepts used

- HTTP requests with the `requests` library
- HTML parsing with `BeautifulSoup`
- Handling encoding issues (UTF-8 vs Latin-1) for special characters
- Extracting data from HTML attributes vs visible text
- Writing structured data to CSV with `csv.DictWriter`

## Notes

This project was built as part of a Python freelance learning roadmap, focused on web scraping as an entry-level freelance skill.
