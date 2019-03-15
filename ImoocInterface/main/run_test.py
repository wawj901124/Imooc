# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/16 10:17'
# import sys
# sys.path.append('E:/www/ImoocInterface')   #将功成目录配置到系统路径下，教程中有，此处多余
import json

from ImoocInterface.base.runmethod import RunMethod   #导入RunMethod
from ImoocInterface.data.get_data import GetData   #导入GetData
from ImoocInterface.util.common_util import CommonUtil   #导入CommonUtil
from ImoocInterface.data.dependent_data import DependdentData   #导入DependdentData
from ImoocInterface.util.send_email import SendEmail   #导入SendEmail
from ImoocInterface.util.operation_header import OperationHeader   #导入OperationHeader
from ImoocInterface.util.operation_json import OperationJson   #导入OperationJson

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()   #实例化
        self.data = GetData()   #实例化
        self.com_util = CommonUtil()   #实例化
        self.send_mai = SendEmail()   #实例化

    #程序执行的
    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []

        #10    0,1,2
        rows_count = self.data.get_case_lines()
        print(rows_count)
        for i in range(1,rows_count):#循环，但去掉第一个
            print("",i)
            is_run = self.data.get_is_run(i)   #获取是否执行
            if is_run:   #如果运行，则执行以下方法
                url = self.data.get_url(i)  # 获取url
                method = self.data.get_request_method(i)  # 获取请求方法
                request_data = self.data.get_data_for_json(i)  # 获取请求数据
                header = self.data.is_header(i)  # 获取是否携带header
                cookie = self.data.is_cookie(i) # 获取是否携带header
                print("header字段内容:",header)
                expect = self.data.get_except_data(i)  # 获取预期结果内容
                depend_case = self.data.is_depend(i)  # 获取是否有case依赖
                # res = self.run_method.run_main(method,url,request_data,header)
                # print(json.dumps(json.loads(res.text),ensure_ascii=False,sort_keys=True,indent=2))#数据格式化处理,sort_keys=True:按照键排序，indent=2之前空两格
            # return res
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)   #实例化
                    #获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key]  = depend_response_data

                if header == 'yes':
                    op_json = OperationJson('../dataconfig/header.json')
                    print("+++++++++++++++++++++++++有header++++++++++++++++++++++++++++++++++")
                    ContentType = op_json.get_data('Content-Type')
                    print("ContentType的内容：",ContentType)
                    header = {
                        'Content-Type': ContentType
                    }
                    if cookie == 'write':
                        print(request_data)
                        res = self.run_method.run_main(method, url, request_data,header)
                        print("***********************有header写cookie************************************")
                        print(res.json())
                        print(res.json()['data'])
                        if res.json()['data']:
                            op_header = OperationHeader(res.json())
                            op_header.write_cookie()
                        else:
                            print("写入cookie失败，请查看请求数据是否正确，响应数据里是否有需要的cookie字段内容！！！")
                    elif cookie == 'yes':
                        op_json = OperationJson('../dataconfig/cookie.json')
                        print("+++++++++++++++++++++++有header，有cookie++++++++++++++++++++++++++++++++++++")
                        cookie = op_json.get_data('apsid')
                        header = {
                            'Content-Type': ContentType,
                            'apsid': cookie
                        }
                        res = self.run_method.run_main(method, url, request_data,header)
                    else:
                        header = {
                            'Content-Type': ContentType
                        }
                        print("+++++++++++++++++++++++有header，无cookie++++++++++++++++++++++++++++++++++++")
                        res = self.run_method.run_main(method, url, request_data, header)
                else:
                    if cookie == 'write':
                        print(request_data)
                        res = self.run_method.run_main(method, url, request_data)
                        print("************************无header，写cookie***********************************")
                        print(res.json())
                        op_header = OperationHeader(res.json())
                        op_header.write_cookie()
                    elif cookie == 'yes':
                        op_json = OperationJson('../dataconfig/cookie.json')
                        print("+++++++++++++++++++++++++无header，有cookie++++++++++++++++++++++++++++++++++")
                        cookie = op_json.get_data('apsid')
                        header = {
                            'apsid': cookie
                        }
                        res = self.run_method.run_main(method, url, request_data,header)
                    else:
                        print("+--------------------------无header，无cookie------------------------------+")
                        res = self.run_method.run_main(method, url, request_data)

                print("实际结果：",json.loads(res.text))

                if self.com_util.is_contain(expect,str(json.loads(res.text))):   #判断预期结果是否在实际结果里，如果包含，则测试通过，否则，测试失败
                    self.data.wirte_result(i,'pass')
                    pass_count.append(i)   #通过的加到集合里
                    print('测试通过')
                else:
                    self.data.wirte_result(i, str(json.loads(res.text)))
                    fail_count.append(i)   #失败的加到集合里
                    print('测试失败')
        # print(len(pass_count))   #打印测试通过数组的个数（长度）
        # print(len(fail_count))   #打印测试失败数组的个数（长度）
        self.send_mai.send_main(pass_count,fail_count)   #调用发送邮件


if __name__ == '__main__':
    run = RunTest()   #实例化
    print('---------------------------')
    run.go_on_run()
    # print(json.dumps(json.loads(run.go_on_run().text),ensure_ascii=False,sort_keys=True,indent=2))  #数据格式化处理,sort_keys=True:按照键排序，indent=2之前空两格
