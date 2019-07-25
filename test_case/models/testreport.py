import time
from test_case.models.RecordLog import log
import unittest
from BeautifulReport import BeautifulReport
from package import HTMLTestRunner
from config import conf


def testreport():
    """

    :return:
    """
    currTime = time.strftime('%Y-%m-%d  %H_%M_%S')
    fileName = conf.reportDir + r"\report" + currTime + ".html"
    try:
        fp = open(fileName,'wb')
    except Exception:
        log.info('[%s] open error cause Failed to generate test report' %fileName)
    else:
        runner = HTMLTestRunner.HTMLTestRunner\
            (stream=fp,title="采购系统测试报告",
                        description="电脑配置待定"
            )
        log.info('successed to generate test report [%s]' %fileName)
        return runner,fp,fileName
def addTc(TCpath = conf.tcPath, rule = '*TC.py'):
    """

    :param TCpath: 测试用例存放路径
    :param rule: 匹配的测试用例文件
    :return:  测试套件
    """
    discover = unittest.defaultTestLoader.discover(TCpath, rule)

    return discover
# 用BeautifulReport模块实现测试报告
def runTc(discover):
    """

    :param discover: 测试套件
    :return:
    """
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    fileName = currTime+'.html'
    try:
        result = BeautifulReport(discover)
        result.report(filename=fileName, description='测试报告', log_path=conf.reportPath)
    except Exception:
        log.logger.exception('Failed to generate test report', exc_info=True)
    else:
        log.logger.info('successed to generate test report [%s]' % fileName)
        return fileName


if __name__ =="__main__":
    testreport()
    suite = addTc(rule='*TC.py')
    runTc(suite)
