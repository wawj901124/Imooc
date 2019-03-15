# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 17:26'

class global_var:
    #case_id
    Id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    cookie = '6'
    case_depend = '7'
    data_depend = '8'
    field_depend = '9'
    data = '10'
    expect = '11'
    result = '12'

#获取caseid
def get_id():
    return global_var.Id

#获取url
def get_url():
    return global_var.url

#获取是否运行
def get_run():
    return global_var.run

#获取运行方式
def get_run_way():
    return global_var.request_way

#获取header所在表的列数
def get_header():
    return global_var.header

#获取cookie
def get_cookie():
    return global_var.cookie

def get_case_depend():
	return global_var.case_depend

def get_data_depend():
	return global_var.data_depend

def get_field_depend():
	return global_var.field_depend

def get_data():
	return global_var.data

def get_expect():
	return global_var.expect

def get_result():
	return global_var.result

#获取header的内容
def get_header_value():
    header = {
        "header":"1234",
        "cookie":"Mushishi"
    }



