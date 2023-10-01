#Python Web Scraper
#https://www.geeksforgeeks.org/python-web-scraping-tutorial/
import requests
from bs4 import BeautifulSoup

url = 'https://www.newegg.com/samsung-1tb-870-evo-series/p/N82E16820147793'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

# Making a GET request
r = requests.get(url, headers=headers)

#check status code for resonse received
#success code - 200
#print(r)

#parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

#finding by id
s = soup.find('div', id = 'app')

pricepanel = s.find('ul', class_= 'price')

# All the li under the above ul
lines = pricepanel.find_all('li')

print(soup.title)

for line in lines:
    print(line.text)
