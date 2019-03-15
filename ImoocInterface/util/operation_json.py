# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/13 16:48'
import json
fp = open('../dataconfig/user.json')   #打开文件
data = json.load(fp)   #加载文件
# print(data['login'])


class OperationJson:

    def __init__(self,file_path=None):#构造函数
        if file_path == None:   #如果file_path为空，则self.file_path为默认写死的路径
            self.file_path = '../dataconfig/user.json'
        else:   #如果传递了file_path，则使用传递的file_path
            self.file_path = file_path
        self.data = self.read_data()  # 获取json文件

            #读取json文件
    def read_data(self):
        with open(self.file_path) as fp:   #使用with，用完文件后会自动关闭文件，不需要fp.close()来关闭文件
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        print("关键字：",id)
        return self.data[id]

    # 写json
    def write_data(self, data):
        with open('../dataconfig/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
    opjson = OperationJson()   #实例化
    print(opjson.get_data('addcart'))


