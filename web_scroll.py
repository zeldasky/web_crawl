import requests
import cfscrape
import csv
import re
from bs4 import BeautifulSoup as bs

scraper = cfscrape.create_scraper()
r = scraper.get("https://www.nanumtrading.com/%EA%B2%BD%EC%A0%9C%EC%A7%80%ED%91%9C%EC%9D%BC%EC%A0%95/")
r.status_code  # 200

text = r.content.decode('utf-8')

html = bs(text, "html.parser")
table = html.find_all('tr')
table = str(table)

html_tag = re.compile('<.*?>')
text = re.sub(html_tag,"", table)

raw_data = text.split(',')

for i in raw_data:
	topic = i.split('\n')
	print(topic)
	
