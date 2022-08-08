import web_scroll as ws
import schedule
import time

def working():
	a = ws.ama_event()

schedule.every().day.at("13:00").do(working)

while True:
    schedule.run_pending()
    time.sleep(1)
