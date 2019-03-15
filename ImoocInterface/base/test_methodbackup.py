# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/12 16:53'
import unittest

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
        print('这是第一个测试方法')
    def test_02(self): #所有的测试方法都必须以test开头，否则执行不了
        print('这是第二个测试方法')


if __name__ == '__main__':
    unittest.main()

