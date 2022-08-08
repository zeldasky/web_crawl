import requests
import json

Token = 'xoxb-3823534486833-3877062023155-3GITdY6AOhLs6BvvE0E7vPlv'

def notice_message(channel, attachments):
    attachments = json.dumps(attachments)
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ Token},
        data={"channel": channel,"attachments": attachments})
        #data={"channel": channel, "text": text ,"attachments": attachments})

if __name__ == '__main__':
    str1_title = 'Test!!'
    attach_dict = {
        'color' : '#ff0000',
        'text' : str1_title,
    }

    attach_list=[attach_dict]
    notice_message("note", attach_list)