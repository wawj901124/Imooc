# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:48'

from ImoocInterface.util.operation_excel import OperationExcel   #导入OperationExcel
from ImoocInterface.data.data_config import *   #导入data_config
from ImoocInterface.util.operation_json import OperationJson   #导入OperationJson


class GetData:
    def __init__(self):
        self.opera_excel = OperationExcel()   #实例化

    #去获取excel行数，就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    #获取是否执行
    def get_is_run(self,row):
        flag = None
        col = int( get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag

    #获取是否携带header
    def is_header(self,row):
        flag = None
        col = int(get_header())
        print("header的列数：",col)
        header = self.opera_excel.get_cell_value(row,col)
        if header != "":
            return header
        else:
            return None

    #获取是否携带cookie
    def is_cookie(self,row):
        flag = None
        col = int(get_cookie())
        print("cookie的列数：",col)
        cookie = self.opera_excel.get_cell_value(row,col)
        if cookie != "":
            return cookie
        else:
            return None

    #获取请求方式
    def get_request_method(self,row):
        col = int( get_run_way() )  #获取请求方式所在的列数
        request_method = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return request_method

    #获取url
    def get_url(self,row):
        col = int( get_url() )  #获取url所在的列数
        url = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        return url

    #获取请求数据
    def get_request_data(self,row):
        col = int( get_data()  ) #获取请求数据所在的列数
        data = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if data == '':
            return None
        else:
            return data

    #通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        opera_json = OperationJson()   #实例化
        request_data = opera_json.get_data(self.get_request_data(row))
        print("从json里获取的请求参数：",request_data)
        print("从json里获取的请求参数的类型：",type(request_data))
        return request_data

    #获取预期结果
    def get_except_data(self,row):
        col = int( get_expect()  )#获取预期结果所在的列数
        except_data = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if except_data == '':
            return None
        else:
            return except_data

    #写入实际结果
    def wirte_result(self,row,value):
        col = int(get_result())   #获取实际结果所在的列数
        self.opera_excel.write_value(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(get_data_depend())
        depent_key = self.opera_excel.get_cell_value(row, col)   #获取指定单元格的内容
        if depent_key == '':
            return None
        else:
            return depent_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(get_case_depend())    #获取数据依赖字段所在列数,应该是获取case依赖那列的数据
        depend_case_id = self.opera_excel.get_cell_value(row, col)  # 获取指定单元格的内容
        if depend_case_id == '':
            return None
        else:
            return depend_case_id


    #获取数据依赖字段
    def get_depend_field(self,row):
        col = int(get_field_depend())    #获取数据依赖字段所在列数,
        data  = self.opera_excel.get_cell_value(row, col)  # 获取指定单元格的内容
        if data == '':
            return None
        else:
            return data



