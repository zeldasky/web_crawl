import requests
import json
import os
import numpy

Token = 'xoxb-3823534486833-3877062023155-IuLx9c1xl3XMC45KgWa6aLNg'

def notice_message(channel, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ Token},
        data={"channel": channel,"attachments": attachments})
        #data={"channel": channel, "text": text ,"attachments": attachments})
