from bs4 import BeautifulSoup
import requests
import csv

response = requests.get('https://books.toscrape.com/?')
response.encoding = 'utf-8'
source = response.text

all_books = []
fields = ['title', 'price', 'availability']
with open('books.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fields)
    writer.writeheader()

    soup = BeautifulSoup(source, 'lxml')
    for article in soup.find_all('article'):
        book = {}
        book['title'] = article.h3.a['title']
        
        book['price'] = article.find('div', class_='product_price').p.text
        
        book['availability'] = article.find('p', class_='instock availability').text.strip()
        
        all_books.append(book)
        
        writer.writerow(book)

        

    