# 下拉刷新的json是怎么构造的…每次都不固定，只有少数字符是固定的

#-*- encoding:utf-8 -*-

import requests
import re
import os

def Huaban_Image(page,directory):
    if not os.path.exists('%s' %directory):
        os.mkdir('%s' %directory)
        os.chdir('%s' %directory)
    image = []
    p = requests.get('%s' %page).content
    pin_pat = re.compile(r'"pin_id":[0-9]{9}')
    key_pat = re.compile(r'"key":"[0-9a-z]{44,46}-[0-9a-zA-Z]{6}", "type":"image/.{3,4}"')
    pin_lst = re.findall(pin_pat,p.decode('utf-8'))
    key_lst = re.findall(key_pat,p.decode('utf-8'))[2:]
    key_lst_1 = [x.replace(',','').replace('"','') for x in key_lst]
    key_lst_2 = [x.split(' ') for x in key_lst_1]
    key_lst_3 = [(x[0][4:],'jpeg') if x[1].endswith('jpeg') else (x[0][4:],'gif') for x in key_lst_2]
    pin_lst_1 = [x[9:] for x in pin_lst]
    for x,y in zip(pin_lst_1,key_lst_3):
        info = dict()
        info['id'] = x
        info['url'] = 'http://img.hb.aicdn.com/' + y[0] + '_fw658'
        info['type'] = y[1]
        image.append(info)
    for x in image:
        req = requests.get(x['url'])
        name = x['id'] + '.' + x['type']
        with open(name,'wb') as f:
            f.write(req.content)
