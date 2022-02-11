#执行测试用例主入口
import datetime
from config.setting import DynamicParam
from utils.logutil import logger
import common.base as Base
import json
import pytest
from utils.readmysql import RdTestcase
from utils.requestsutil import RequestSend

#初始化类
attribute = DynamicParam()

#实例化测试用例对象
case_data = RdTestcase()
