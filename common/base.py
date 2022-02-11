import json
from string import Template #用于转换格式为str并固定格式
import re #re模块主要功能是通过正则表达式是用来匹配处理字符串的

#根剧参数匹配内容
def find(data):
    #判断data类型是否为字典
    if isinstance(data,dict):
        #对象格式化为json字符串，类型为str
        data = json.dumps(data)
        #定义正则匹配规则
        pattern = "\\${.*?}"
        #按匹配进行查询，把查询的结果返回
        return re.findall(pattern,data)

#进行参数替换
def relace(ori_data,replace_data):
    #对象格式化为str
    ori_data = json.dumps(ori_data)
    #处理字符串的类，实例化并初始化为原始字符，ori_data--》s
    s = Template(ori_data)
    #使用新的字符串替换，s--》replace_data
    return s.safe_substitute(replace_data)

#根剧var，逐层获取json格式的值
def parse_relation(var,resdata):
    #判断变量var是否存在
    if not var:
        return resdata
    else:
        #如果var存在，则获取数组第一个内容
        resdata = resdata.get(var[0])
        #从数组中删除第一个内容
        del var[0]
        #递归
        return parse_relation(var,resdata)

#测试代码
if __name__ == '__main__':
    ori_data = {"admin-token":"${token}"}
    replace_data = {'token':'x015k878'}
    print(relace(ori_data,replace_data))