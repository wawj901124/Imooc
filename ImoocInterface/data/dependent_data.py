# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/16 15:16'
import json

from jsonpath_rw import jsonpath,parse  #导入jsonpath,parse（比对的）

from ImoocInterface.util.operation_excel import OperationExcel   #导入OperationExcel
from ImoocInterface.base.runmethod import RunMethod   #导入RunMethod
from ImoocInterface.data.get_data import GetData   #导入GetData
from ImoocInterface.util.operation_json import OperationJson   #导入OperationJson

#处理所有数据依赖的类
class DependdentData:
    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()   #实例化
        self.data = GetData()   #实例化


    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()   #实例化
        row_num = self.opera_excel.get_row_num(self.case_id)   #获取行号
        request_data = self.data.get_data_for_json(row_num)   #获取请求数据
        header = self.data.is_header(row_num)   #获取是否传入header
        print(header)
        print(type(header))
        if header == 'yes':
            op_json = OperationJson('../dataconfig/header.json')
            print("+++++++++++++++++++++++++有header++++++++++++++++++++++++++++++++++")
            ContentType = op_json.get_data('Content-Type')
            print("ContentType的内容：", ContentType)
            header = {
                'Content-Type': ContentType
            }
        else:
            header = None
        method = self.data.get_request_method(row_num)   #获取请求方式
        url = self.data.get_url(row_num)   #获取请求url
        res = run_method.run_main(method,url,request_data,header)
        return res

    #难点：根据依赖的key去获取执行依赖测试case的响应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        print('depend_data************:', depend_data)
        print(type(depend_data))
        response_data = self.run_dependent()   #拿到响应值
        print('response_data************1:', response_data)
        response_data = json.loads(response_data.text)   #字符串转换为字典
        print(type(response_data))
        print('response_data************2:',response_data)
        json_exe = parse(depend_data)   #建立规则
        madle = json_exe.find(response_data)   #在response_data找符合规则的数据，madle是个结果集
        print('madle*************:',madle)
        print('[math.value for math in madle][0]**********************:',[math.value for math in madle][0])
        return [math.value for math in madle][0]   #增强for循环写法固定，其中math为字典类型

