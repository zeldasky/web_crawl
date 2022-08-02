import slack_notice as sl
import requests
import cfscrape
import csv
import re
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta

date = '1월1일'
time = '09:30'
time_format = "%m월%d일 %H:%M"

subscribe = ['FOMC', 'GDP', 'CPI', 'PPI']

def send_message(title, before, now):
	datetime_result = datetime.strptime(date+' '+time, time_format)
	korea_time = datetime_result + timedelta(hours=13)
	text_date = korea_time.strftime("%m/%d %H:%M")
	attach_dict = {'text' : str(text_date)+' (한국시간)'+'\n'+title+'\n'+'예상: '+before+'\n'+'이전: '+now}
	attach_list=[attach_dict]
	sl.notice_message("notice_economy", attach_list)

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

data = []
new_data = []

for i in raw_data:
	topic = i.split('\n')
	data.extend([topic])

for i in data:
	temp = i
	for index, j in enumerate(temp):
		if index == 1 and j.find('월') != -1 and j.find('일') != -1 and j != '월요일':
			date = j
			continue
		if j == 'USD':
			title = temp[3]
			for a in subscribe:
				if title.find(a) != -1:
					time = temp[1]
					before = temp[5]
					now = temp[6]
					send_message(title, before, now)




