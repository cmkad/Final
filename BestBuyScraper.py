#BestBuy Web Scraper

import requests
from bs4 import BeautifulSoup

url = 'https://www.bestbuy.com/site/samsung-870-evo-1tb-internal-ssd-sata/6447127.p?skuId=6447127'
HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
#Makeing a GET request
r = requests.get(url, headers=HEADERS)

#check status code for resonse received
#success code - 200
#print(r)

#parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

#finding by id (this line of code is uneeded. Finding by id, the id name changed each time)
#s = soup.find('div', id = 'pricing-price')

pricepanel = soup.find('div', class_= 'priceView-hero-price priceView-customer-price')

lines = pricepanel.find_all('span')

print(soup.title)

for line in lines:
    print(line.text)
