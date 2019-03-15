# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/16 11:39'
import json

class CommonUtil:
    def is_contain(self,str_one, str_two):
        '''
        判断一个字符串是否在另外一个字符串中
        :param str_one:查找的字符串
        :param str_two:被查找的字符串
        :return:返回布尔值
        '''
        flag = None
        print('第一个参数：',str_one)
        print('第一个参数类型：',type(str_one))
        print('第二个参数：',str_two)
        print('第二个参数类型：',type(str_two))

        if str_one in str_two:
            flag = True;
        else:
            flag = False
        return flag

    def is_equal(self,dict_one,dict_two):
        """
        判断两个字典是否相等
        :param dict_one:
        :param dict_two:
        :return:
        """
        if isinstance(dict_one,str):   #如果是字符串，则转换为字典
            dict_one = json.loads(dict_one)   #将字符串转为字典
        if isinstance(dict_two,str):   #如果是字符串，则转换为字典
            dict_two = json.loads(dict_two)   #将字符串转为字典
        return cmp(dict_one,dict_two)#判断两个字段是不是相同的系统函数


