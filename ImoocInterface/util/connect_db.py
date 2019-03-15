# _*_ coding:utf-8 _*_

__author__ = 'bobby'
__date__ = '2018/7/25 17:36'

import pymysql
import json

conn = pymysql.connect(host="localhost", user="root", passwd="root", port=3306, db="imoc",charset="utf8")
cursor = conn.cursor()
sql = "SELECT * FROM web_user WHERE Name='mushishi' "
cursor.execute(sql)
res = cursor.fetchall()
print(res)
cursor.close()
conn.close()

class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            port=3306,
            db="imoc",
            charset="utf8",
            cursorclass = pymysql.cursors.DictCursor    #保证获取到的数据库的值为键值对的形式，字典类型
        )
        self.cur = self.conn.cursor()

    #查询一条数据
    def search_one(self,sql):
        self.cur.execute(sql)   #执行查询语句
        result = self.cur.fetchall()   #获取结果
        result = json.dumps(result)   #将获取到的字典类型的值转为字符串类型
        return  result   #返回结果

if __name__ == '__main__':
    op_mysql = OperationMysql()   #实例化
    sql = "SELECT * FROM web_user WHERE Name='mushishi' "
    result = op_mysql.search_one(sql)
    print(result)
    print(type(result))