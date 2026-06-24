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




# RemoteOK Job Scraper

A Python web scraper that collects remote job listings from RemoteOK and exports them to a CSV file.

## Overview

This project scrapes remote job postings from RemoteOK by discovering and using the site's paginated job endpoint. The scraper extracts key job information and stores it in a structured CSV file for further analysis.

The project demonstrates:

* Network request inspection using browser DevTools
* Pagination handling
* HTML parsing with BeautifulSoup
* Data extraction and cleaning
* CSV export
* Handling missing data fields

## Features

* Scrapes over 1000 remote job listings
* Handles paginated results automatically
* Extracts:

  * Job Title
  * Company Name
  * Location
  * Salary (when available)
  * Job Tags
  * Job URL
  * Date Posted
* Exports results to a CSV file
* Uses UTF-8 encoding for proper text handling

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* CSV Module
* lxml Parser

## Installation

Clone the repository:

```bash
git clone https://github.com/Salumohammedawal/web-scraping.git
cd remoteok-job-scraper
```

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml
```

## Usage

Run the scraper:

```bash
python jobs.py
```

The scraper will create:

```text
job_listings.csv
```

containing all collected job records.

## How It Works

Initially, scraping the main website returned only limited information. Using browser Developer Tools, the network requests were inspected to identify the endpoint responsible for loading job data.

The scraper sends requests to the paginated endpoint and iterates through offsets to collect multiple pages of job listings.

Example pagination pattern:

```text
offset=0
offset=50
offset=100
...
```

Each page is parsed and relevant job information is extracted and written to a CSV file.

## Sample Output

| Job Title        | Company Name | Location  | Salary       |
| ---------------- | ------------ | --------- | ------------ |
| Python Developer | Example Corp | Worldwide | $80k-$120k   |
| Data Engineer    | Tech Inc     | Remote    | Not Provided |

## Notes

The source pagination occasionally contains overlapping records between pages. During testing:

* Total rows scraped: 1016
* Unique jobs: 1009

This results in a duplicate rate below 1%, which is acceptable for this learning project.

## Learning Outcomes

Through this project I practiced:

* Reverse engineering data sources
* Working with paginated content
* Extracting structured data from HTML
* Building reusable scraping workflows
* Exporting data for analysis

## Disclaimer

This project was created for educational purposes. Please review the target website's Terms of Service before using the scraper at scale.

