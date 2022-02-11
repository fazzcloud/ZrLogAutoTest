#测试用例读取工具类
import datetime
import json
from utils.mysqlutil import MysqlUtil
from utils.logutil import logger

#实例化mysql对象
mysql = MysqlUtil()

#定义获取测试用例工具类
class RdTestcase:
    #加载所有测试用例
    def load_all_case(self,web):
        #定义sql语句，where web = 传入的web
        sql = f"select * from test_case_list where web = '{web}'"
        #调用数据库工具类方法，返回所有数据
        results = mysql.get_fetchall(sql)
        return results

    #筛选可执行的用例
    def is_run_data(self,web):
        #根剧条件 isdel == 1筛选可执行的测试用例
        '''
        这里使用的是列表解析，
        格式为[expr for iter_var in iterable if cond_expr]，将函数load_all_case返回的结果看作一个列表
        生成新的列表case
        条件为，case列表中‘isdel’元素的值为1（每一列就被视为一个元素，值就是表中存放的数据）
        '''
        run_list = [case for case in self.load_all_case(web) if case['isdel'] == 1 ]
        return run_list

    #获取配置信息,
    def loadConfkey(self,web,key):
        #根剧项目名和key获取对应环境信息
        sql = f"select * from test_config wher web = '{web}' and key = '{key}'"
        #调用方法查询一条结果
        results = mysql.get_fetchone(sql)
        return results

    #更新测试结果
    def updateResults(self,response,is_pass,case_id):
        #获取当前时间
        current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #跟新测试用例执行结果，插入test_result_record表,这里注意需要用json.dumps将返回结果转化为json格式
        sql = f"insert into test_result_record (case_id,times,response,result) values('{case_id}','{current_time}','{json.dumps(response,ensure_ascii=False)}','{is_pass}')"
        #执行insert操作，调用更新数据函数
        rows = mysql.sql_execute(sql)
        #打印日志
        logger.debug(sql)
        #返回结果
        return rows

#测试代码
if __name__  ==  '__main__' :
        test = RdTestcase()
        res = test.updateResults({
            'code': 200,
            'body': {
                'error': 1,
                'message': '用户名和密码都不能为空'},
            'cookies': {}
        }, 'True', '4565'
        )
        print(res)






