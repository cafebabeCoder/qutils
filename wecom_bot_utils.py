# encoding: utf-8
import requests
import time
import json

bot_webhook = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=9f6f72c3-eea3-4a25-9a9c-cdbc7e718ea2'

def post_text_message(text):
    data = {
        "msgtype": "text",
        "text": {
            "content": text,
        }
    }
    headers = {'content-type': 'application/json'}

    is_success = False
    for retry in range(3):
        req = requests.post(bot_webhook, data=json.dumps(data), headers=headers)
        if req.status_code == 200:
            is_success = True
            break

    return is_success

def post_markdown_message(markdown):
    pass

if __name__ == '__main__':
    pass