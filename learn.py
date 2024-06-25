import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract quotes, authors, and tags
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

# Print the extracted information
for quote, author, tag in zip(quotes, authors, tags):
    print(f'Quote: {quote.text}')
    print(f'Author: {author.text}')

    tag_list = tag.find_all('a', class_='tag')
    print('Tags:', ', '.join([t.text for t in tag_list]))

    print()  
