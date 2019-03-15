# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/24 14:40'
import  requests
import json

cookies = {
    "apsid":""   #cookies 信息
}

list_data = json.dumps([{},{}])   #json转义

# data = {
#     "goods_ids":list_data
# }
data = {
    "uid":"5249191"
}

# url = "http://order.imooc.com/pay/check"
url = "https://m.imooc.com/api/user/ajaxusercheck?uid=5249191"
# res = requests.post(url=url,data=data,cookies = cookies).text
res = requests.post(url=url,data=data,verify=False).text   #verify=False:https默认证书忽略掉
# res = requests.post(url=url,data=data).text #verify=False:https默认证书忽略掉
print(res)