import os
from datetime import datetime
from test_case.models.CreatePath import ModelsClass
#项目根目录
projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#配置文件所在目录

configDir = os.path.join(projectDir,"config","config.ini")

#报告目录
reportDir = os.path.join(projectDir,"report","TestReport")


LOG_NAME = ModelsClass.file_name('log')

#日志目录
logPath = os.path.join(projectDir,"report","Log")

CREATE_LOG_DIR = ModelsClass.create_dir(logPath)

LOG_PATH = os.path.join(logPath,LOG_NAME)
#测试用例路径
tcPath = os.path.join(projectDir,"test_case")

#获取测试报告路径
dataPath = os.path.join(projectDir,"data","TestData","tcData.xlsx")

#保存截图路径
#错误截图
failImagePath = os.path.join(projectDir,"report","image","fail")

#成功截图
passImagePath = os.path.join(projectDir,"report","image","pass")

