# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 15:06'

from mock import mock   #导入mock，模拟结果返回

#模拟mock封装
def mock_test(mock_method, request_data, url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)  # 使用mock模拟返回response_data值
    res = mock_method(url,method,request_data)
    return res

