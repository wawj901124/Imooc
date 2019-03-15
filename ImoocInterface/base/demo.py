import requests
import json


class RunMain:
    def __init__(self, url, method, data=None):
        self.res = self.run_main(url, method, data)

    def send_get(self, url, data):
        res = requests.get(url=url, data=data)
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data)
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == "GET":
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        print(res.text)
        return res


if __name__ == '__main__':
    # url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'

    url = 'https://show-3.mediav.com/s?jsonp=success_mv_right&showid=GGdtgu&type=1&of=4&newf=1&uid=26070691110208271115313908034555&queryword=&mid=5dffe47064411aa28d8a861982f4ff17&impct=1&ref=&_=1531390803162'

    # data = {
    #     'cart': '11'
    # }
    run = RunMain(url, "GET")
    print(run.res)



