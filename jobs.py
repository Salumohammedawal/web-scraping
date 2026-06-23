from bs4 import BeautifulSoup
import requests
import csv

header = {'User-Agent': 'Mozilla/5.0'}

all_jobs = []
fields = [
    'Job Title',
    'Company Name',
    'Location',
    'Salary',
    'Job Tags',
    'Job URL',
    'Date Posted'
]

with open('job_listings.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()

    offset = 0

    while True:
        url = f'https://remoteok.com/?action=get_jobs&premium=0&pagination=1&offset={offset}'

        response = requests.get(url, headers=header)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all('tr', class_='job')

        if len(jobs) == 0:
            break

        print(f'Offset {offset}: {len(jobs)} jobs found')

        for job in jobs:
            work = {}

            work['Job Title'] = job.find('h2').text.strip()
            work['Company Name'] = job.find('h3').text.strip()
            work['Location'] = job.find('div', class_='location').text.strip()

            salary = job.find('div', class_='salary')
            work['Salary'] = salary.text.strip() if salary else 'Not Provided'

            tags = job.find('td', class_='tags')
            tag_list = []

            for t in tags:
                text = t.text.strip()
                if text:
                    tag_list.append(text)

            work['Job Tags'] = ', '.join(tag_list)

            work['Job URL'] = 'https://remoteok.com' + job.get('data-href')

            date = job.find('time')
            work['Date Posted'] = date.get('datetime')

            all_jobs.append(work)
            writer.writerow(work)

        offset += 50

print(f'Total jobs scraped: {len(all_jobs)}')

urls = [job['Job URL'] for job in all_jobs]

print(f'Total rows: {len(urls)}')
print(f'Unique rows: {len(set(urls))}')