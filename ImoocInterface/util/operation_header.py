# # _*_ coding:utf-8 _*_
#
# __author__ = 'bobby'
# __date__ = '2018/7/24 15:41'
# import requests
#
# url = "https://m.imooc.com/passport/user/login"
# data = {
#     "username":"15035490862",
#     "password":"12345678",
#     "verify":"",
#     "pwencode":"1",
#     "referer":"https://m.imooc.com"
# }
#
# res = requests.post(url,data,verify =False).json()
# print(res)
#
# request_url = "https://www.imooc.com/user/ssologin?token=Pku2RYyBjzDnfDkHR1vVg0H_-XwhGeAV4sPtxugh56KQ6DgELZAIOfyF7lZEu0ukkhB7yN38576ex_ZoXW6jO4d6v1nKe-pna0qIvyMKgpmy_Y4VIARriQDCG5AGJJ06FuC95K7O9t67xMCxtRzbeoBH0ZjHE24HKaZSGysaG9bpL9n6icAONFVSI_kLYQRB2TBk9rDd-nhwsiVM5vtmSdp-nG3vEVo24uIXrBRAO5mUrFZXOGn_x8ccTlpyucHJ-lAGFZaJDM&callback=jQuery21008452618959082887_1532418865215&_=1532418865216"
#
# cookies = requests.get(request_url,verify=False).cookies   #获取cookies
# # print(cookies)
# # cookies = requests.utils.dict_from_cookiejar(cookies)   #将cookies从CookieJar的形式转换为字典形式，便于存储
# # print(cookies)
# # print(type(cookies))
# # print(cookies['apsid'])
# # print(cookies['cvde'])
# url1 = 'https://www.imooc.com/static/moco/v1.0/dist/css/moco.min.css'
# print(requests.get(url=url1,cookies=cookies,verify=False).text)
import requests
import json
from ImoocInterface.util.operation_json import OperationJson


class OperationHeader:

    def __init__(self, response):
        print(type(response))
        self.response = response
        # self.response = json.loads(response)

    def get_response_url(self):
        '''
        获取登录返回的token的url
        '''
        url = self.response['data']['url'][0]
        return url

    def get_cookie(self):
        '''
        获取cookie的jar文件
        '''
        url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        cookie = requests.get(url).cookies
        return cookie

    def write_cookie(self):
        """
        存储cookie到cookie.json文件中
        """
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())   #将cookies从CookieJar的形式转换为字典形式，便于存储
        print(cookie)
        op_json = OperationJson()
        op_json.write_data(cookie)
        print("cookie字段写入完成.")




if __name__ == '__main__':
    url = "http://m.imooc.com/passport/user/login"
    # data = {
    #     "username": "18513199586",
    #     "password": "111111",
    #     "verify": "",
    #     "referer": "https://m.imooc.com"
    # }
    data = {
        'username': '18513199586',
        'password': '111111',
        'verify': '',
        'referer': 'https://m.imooc.com'
    }
    res = json.dumps(requests.post(url, data).json())
    print(res)
    op_header = OperationHeader(res)
    op_header.write_cookie()