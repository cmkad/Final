#Amazon Web Scraper
#Using https://www.scrapingbee.com/blog/web-scraping-amazon/
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/SAMSUNG-Inch-Internal-MZ-77E1T0B-AM/dp/B08QBJ2YMG"

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

r = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.title)
title = soup.find('span', {'id':"productTitle"}).text.strip()
price = soup.find('span', {'class':"a-offscreen"}).text.strip()

print(title)
print(price)



# s = soup.find('div', id = 'corePrice_feature_div')
# price = s.find('span', class_="a-offscreen")
# lines = price.find_all('span')
# for line in lines:
#     print(line.text)