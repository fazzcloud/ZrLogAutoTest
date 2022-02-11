#存放配置信息
#config=utf-8
#导入os库,操作目录及文件
import os

#获取文件的绝对路径
abs_path = os.path.abspath(__file__)
#print(abs_path)

#获取文件所在目录的上一级目录，也就是根目录
project_path = os.path.dirname(os.path.dirname(__file__))
#print(project_path)

#通过os.sep方法获取config,log,report目录的全路径
_conf_path =  project_path + os.sep + "config"
_log_path =  project_path + os.sep + "log"
_report_path =  project_path + os.sep + "report"

#数据库信息配置
DB_CONFIG = {
    "host" : "106.14.135.177",
    "port" : 3306,
    "user" : "root",
    "password" : "lj19950104",
    "database" : "test",
    "charset" : "utf8"
}

#返回config目录
def get_config_path():
    return _conf_path

#返回日志目录
def get_log_path():
    return _log_path

#返回报告目录
def get_report_path():
    return _report_path

#占位用，勿删除
class DynamicParam:
    pass

#测试代码：
if __name__ == "__main__":
    print("config路径为：",get_config_path())
    print("log路径为：",get_log_path())
    print("report路径为：",get_report_path())
