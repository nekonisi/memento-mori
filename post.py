#!/usr/bin/env python
#coding: UTF-8
import requests
import json
import const

# headerを定義
headers = {
        'Authorization': 'Bearer ' + const.TOKEN,
        'Content-Type' : 'application/json'
        }

# json形式でメッセージを定義
message_list = {
        'messages' : [
            {
                'type':'text',
                'text':'memento mori'
                }
            ]
        }

# jsonにエンコード
data = json.dumps(message_list)
response = requests.post(url, headers=headers, data=data)
