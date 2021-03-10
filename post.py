#!/usr/bin/env python
#coding: UTF-8
import requests
import json
import random
import const

url = 'https://api.line.me/v2/bot/message/broadcast'

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

#tmp読み込み
f = open('/home/pi/memento_mori/tmp', 'r')
tmp = f.read()
f.close

#乱数生成
rand = random.randint(0, int(tmp))
if tmp == '1' or tmp == '':
    f = open('/home/pi/memento_mori/tmp', 'w')
    f.write(str(const.FREQUENCY))
    f.close
elif rand == 1:
    data = json.dumps(message_list)
    response = requests.post(url, headers=headers, data=data)
    f = open('/home/pi/memento_mori/tmp', 'w')
    f.write(str(const.FREQUENCY))
    f.close
else:
    f = open('/home/pi/memento_mori/tmp', 'w')
    f.write(str(int(tmp) - 1))
    f.close
