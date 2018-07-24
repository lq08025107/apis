#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import web
import china
import json
import random
urls = (
    '/hello', 'hello',
    '/provinces', 'provinces',
    '/citys', 'citys',
    '/levels', 'levels',
    '/completion', 'completion'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'
class provinces:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        datas = json.loads(china.data)
        provinces = {}
        for data in datas['provinces']:
            temp = data['provinceName']
            if temp.find("壮族自治区") != -1:
                temp = temp1 = temp.replace("壮族自治区","")
            if temp.find("回族自治区") != -1:
                temp = temp1 = temp.replace("回族自治区","")
            if(temp.find("维吾尔自治区")) != -1:
                temp = temp1 = temp.replace("维吾尔自治区","")
            if temp.find("自治区") != -1:
                temp = temp1 = temp.replace("自治区","")
            if temp.find("省") != -1:
                temp = temp1 = temp.replace("省","")
            if temp.find("市") != -1:
                temp = temp1 = temp.replace("市","")

            provinces.setdefault(temp1, random.randint(1,1000))
        p = json.dumps(provinces,ensure_ascii=False)
        print p
        return p
class citys:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        provinceName = web.input().name
        result = {}
        datas = json.loads(china.data)
        city = {}
        for data in datas['provinces']:
            if data['provinceName'].find(provinceName) != -1:
                city = data['citys']
            else:
                pass
        for c in city:
            cityName = c['citysName']
            result.setdefault(cityName, random.randint(1,100))
        c = json.dumps(result,ensure_ascii=False)
        print c
        return c
class levels:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        result = {}
        result.setdefault("highest", random.randint(1,100))
        result.setdefault("high", random.randint(50,100))
        result.setdefault("middle", random.randint(200,500))
        result.setdefault("low", random.randint(200,700))
        c = json.dumps(result, ensure_ascii=False)
        print c
        return c
class completion:
    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        c = random.randint(60, 100)
        print c
        return c;
if __name__ == "__main__":
    app.run()
