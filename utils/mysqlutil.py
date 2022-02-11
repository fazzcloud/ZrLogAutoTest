#数据库工具类
import pymysql
#导入数据库配置信息
from config.setting import DB_CONFIG
#导入log
from utils.logutil import logger

#设置数据库工具类
class MysqlUtil:

    #初始化自身函数：获取数据库连接，创建游标
    def __init__(self):
        #创建db对象获取数据库连接信息
        self.db = pymysql.connect(**DB_CONFIG)
        #创建数据库游标
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    #定义函数获取单条数据
    def get_fetchone(self,sql):
        #执行sql
        self.cursor.execute(sql)
        #返回单条执行结果
        return self.cursor.fetchone()

    #定义函数获取多条数据
    def get_fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    #执行更新操作函数
    def sql_execute(self,sql):
        try:
            #游标和db对象都存在，也就是代表正在正常操作数据库
            if self.db and self.cursor:
                self.cursor.execute(sql)
                self.db.commit()#提交数据
        except Exception as e:
            #异常则数据回滚
            self.db.rollback()
            #打印异常日志
            logger.error("sql语句执行错误，已执行回滚操作")
            #返回结果
            return False

    @staticmethod #静态方法
    def close(self):
        #判断数据库对象和游标是否存在，存在则关闭
        if self.cursor is not None:
            self.cursor.close()
        if self.db is not None:
            self.db.close()

#测试代码
if __name__ == "__main__":
    mysql = MysqlUtil()
    res = mysql.get_fetchall("select * from test_case_list")
    #res = mysql.sql_execute("insert into test_result_record (case_id,times,response,result) values('4565','2022-02-10 16:06:06','{\"code\": 200, \"body\": {\"error\": 1, \"message\": \"用户名和密码都不能为空\"}, \"cookies\": {}}','True')")
    print(res)



