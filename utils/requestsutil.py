#HTTP请求工具类
import requests
from utils.logutil import logger
from utils.readmysql import RdTestcase

#定义HTTP请求类
class RequestSend:
    #封装request请求函数
    def api_run(self,url,method,data=None,headers=None,cookies=None):
        #定义变量，获取响应结果，默认值为None
        res = None
        #打印日志
        logger.info(f"请求的url为{url}，类型为{type(url)}")
        logger.info(f"请求的method为{method}，类型为{type(method)}")
        logger.info(f"请求的data为{data}，类型为{type(data)}")
        logger.info(f"请求的headers为{headers}，类型为{type(headers)}")
        logger.info(f"请求的cookies为{cookies}，类型为{type(cookies)}")

        #判断请求方法
        if method == "get":
            res = requests.get(url,data=data,headers=headers,cookies=cookies)
        elif method == "post":
            #判断数据类型是否是json格式
            if headers == {"Content-Type":"application/json"}:
                res = requests.post(url,json=data,headers=headers,cookies=cookies)
            #若不是json格式，参数使用data=data
            elif headers == {"Content-Type":"application/x-www-form-urlencoded"}:
                res = requests.post(url,data=data,headers=headers,cookies=cookies)

        #获取请求响应的状态码
        code = res.status_code
        #获取请求响应的cookie
        cookies = res.cookies.get_dict()
        #定义字典
        dict1 = dict()
        try:
            #获取响应结果json格式
            body = res.json()
        except:
            body = res.text
        #自定义参数写入字典
        dict1['code'] = code
        dict1['body'] = body
        dict1['cookies'] = cookies

        return dict1

    #对外调用方法，**kwargs传入的参数是dict类型
    def send(self,url,method,**kwargs):
        #调用自定义方法
        return self.api_run(url=url,method=method,**kwargs)

#测试代码
if __name__ == '__main__':
    url = 'http://106.14.135.177/api/admin/login'
    data = {"userName":"admin","password":123456,"https":False,"key":1598188173501}
    method = "post"
    headers = {"Content-Type":"application/json"}
    print(RequestSend().send(url=url,method=method,headers=headers,data=data))
