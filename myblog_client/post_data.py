#coding: utf-8
import requests
import json
def post_data():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"name":4,"sn_num":'123sds4',"remark":'数据1'}
    url = 'http://127.0.0.1:8080/service_info/'
    cent = requests.post(url, data=json.dumps(data), headers=headers)
    print(cent.content)

post_data()