from test_case.models.driver import WDriver
import logging
import unittest
from test_case.page_object.login_page import LoginPage
from test_case.models.RecordLog import log


class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):#一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()
        log.info("opened the browser successed!")


    def setUp(self):
        """

        :return:
        """
        self.login = LoginPage(self.driver)
        self.login.open()
        log.info('************************starting run test cases************************')

    def tearDown(self):
        """

        :return:
        """
        self.driver.refresh()
        log.info('************************test case run completed************************')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info('quit the browser success!')

if __name__ == "__main__":
    unittest.main()