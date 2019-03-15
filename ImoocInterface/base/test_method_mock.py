# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/12 16:53'
import json
import unittest

import HTMLTestRunner
from mock import mock   #导入mock

from ImoocInterface.base.demo import RunMain
from ImoocInterface.base.mock_demo import mock_test


class TestMethod(unittest.TestCase):  #创建测试类
    @classmethod            #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为setUpClass
    def setUpClass(cls):
        print('类执行之前的方法')

    @classmethod            #类方法，只执行一次，但必须要加注解@classmethod,且名字固定为tearDownClass
    def tearDownClass(cls):
        print('类执行之后的方法')

   #每次方法之前执行
    def setUp(self):   #每条用例执行测试之前都要执行此方法
        print('test-->setup')
    #每次方法之后执行
    def tearDown(self):
        print('test---->teardown')

    def test_01(self): #所有的测试方法都必须以test开头，否则执行不了
        url = 'https://show-3.mediav.com/s?jsonp=success_mv_right&showid=GGdtgu&type=1&of=4&newf=1&uid=26070691110208271115313908034555&queryword=&mid=5dffe47064411aa28d8a861982f4ff17&impct=1&ref=&_=1531390803162'
        data = {}
        self.run = RunMain(url,'GET',data)
        res = self.run.run_main(url,'GET',data)
        print(res)
        print('这是第一个测试方法')
        globals() ['userid']= '1000909'   #定义全局变量userid

    # @unittest.skip('test_02')   #跳过用例名字为‘test_02’的用例，跳过的用例的执行结果显示：是
    def test_02(self): #所有的测试方法都必须以test开头，否则执行不了
        print('userid=',userid)  #使用全局变量userid
        url = 'http://coding.imooc.com/api/cate'
        request_data = {
            'timestamp': '1507034803124',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '7d6f14f21ec96d755de41e6c076758dd',
            'cid': '0'
        }
        response_data = {
            "status":1,
            "data":[],
            "errorCode":1007,
            "errorDesc":"token expire",
            "timestamp":1531466987357
        }
        self.run = RunMain(url,'POST',request_data)   #实例化
        res = mock_test(self.run.run_main,request_data,url,'POST',response_data)   #调用自定义的mock_test方法
        print('这是第二个测试方法')
        self.assertEqual(res["errorCode"],1007,'测试失败')  #不相等时报‘测试失败’


if __name__ == '__main__':
    #使用unittest.main()跑
    unittest.main()

    #使用unittest.TextTestRunner().run(suite) 跑
    # suite = unittest.TestSuite()  #创建一个用例容器
    # suite.addTest(TestMethod('test_01'))
    # # suite.addTest(TestMethod('test_02'))   #往容器里添加case,添加用例名字为test_02的用例
    # unittest.TextTestRunner().run(suite)   #执行用例集suite

    # #使用HTMLTestRunner跑
    # filepath = "./report/htmlreport.html"   #放置报告的路径
    # fp = open(filepath,'wb')   #资源流,以读写的方式打开 file用open替代即可
    # suite = unittest.TestSuite()  #创建一个用例容器
    # suite.addTest(TestMethod('test_01'))
    # suite.addTest(TestMethod('test_02'))   #往容器里添加case,添加用例名字为test_02的用例
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='this is a report',description='report description')   #设置报告的标题和描述
    # runner.run(suite)  #执行用例集suite