# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/16 10:02'

import requests


class RunMethod:
    def post_main(self,url,data,header=None):   #header可以为空
        res = None
        if header !=None:
            res = requests.post(url=url, data=data,headers = header,verify =False) #verify=False:https默认证书忽略掉
        else:
            res = requests.post(url=url,data=data,verify =False)
            print(res.status_code)   #status_code:返回接口响应的状态码，一般200为接口正常，但不能判断响应的接口数据是否正确
        return res

    def get_main(self,url,data=None,header=None):   #data可以为空
        res = None
        if header !=None:
            res = requests.get(url=url, data=data,headers=header,verify =False)#verify=False:https默认证书忽略掉
        else:
            res = requests.get(url=url,data=data,verify =False)
        return res


    def run_main(self,method,url,data=None,header=None):   #header和data都可以为空
        res = None
        if method == 'post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url, data, header)
        return res