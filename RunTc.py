import unittest
from config.conf import *
from test_case.models.testreport import testreport
from BeautifulReport import BeautifulReport
import time

# TODO : will be use jenkins continuous intergration teachnology manage the auto project


if __name__ == "__main__":
    currTime = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = currTime + '.html'
    # 第一种测试报告
    test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='LoginTc.py')
    result = BeautifulReport(test_suite)
    result.report(filename= filename, description='test report', log_path=reportDir )

    # runner,fp,fileName = testreport()
    # test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='LoginTc.py')
    # runner.run(test_suite)
    # fp.close()
