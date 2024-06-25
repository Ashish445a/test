import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
responce = requests.get(url)
#print(responce.content)
soup = BeautifulSoup(responce.content, 'html.parser')
#print(soup)
# # # Extract quotes , authors, and tags
quotes = soup.find_all('span' , class_='text')
authors = soup.find_all('small' , class_='authors')
tags = soup.find_all('div' , class_='tags')

# # # Print the extracted information
for quotes , author ,tag in zip(quotes,authors,tags):
    print(f'Quotes: {quotes.text}')
    print(f'Authors: {author.text}')
    print('Tags:')
    for t in tag.find_all('a' , class_='tags'):
        print(f' - {t.text}')
    print()
    