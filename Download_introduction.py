import urllib.request
urllib.request.urlretrieve("https://grad.ucla.edu/asis/agep/advcv.pdf","new.pdf")

import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('https://viphouse.rs/products/27031/6360.jpg').read()
fhand = open('6360.jpg', 'wb')
fhand.write(img)
fhand.close()

import requests
from b4 import BeautifulSoup
def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'item-name'}):
        href = "https://buckysroom.org" + link.get('href')
        title = link.string
        print(href)
        print(title)
    page += 1   
trade_spider(1)

import requests
from b4 import BeautifulSoup


def trade_spider(max_pages):
  page = 1
  while page <= max_pages:
    url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a', {'class': 'item-name'}):
        href = "https://buckysroom.org" + link.get('href')
        title = link.string
        # print(href)
        # print(title)
        get_single_item_data(href)
    page += 1
    

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)

trade_spider(3)
