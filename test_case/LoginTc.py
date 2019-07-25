import unittest
import time
from test_case.models.RecordLog import log
from test_case.models.myunit import MyunitTest

class Login_TC(MyunitTest):
    """登录模块测试用列"""

    def test_login_success_correct_username_password(self):
        """用户名正确，密码正确，登录成功"""
        self.login.loginFunc()
        time.sleep(2)
        currUrl = self.driver.current_url#获取当前的url地址
        self.login.delete_all_cookies()

        try:
            self.assertIn("home",currUrl,"main not in current  url")
        except Exception:
            self.login.saveScreeenShot("correct_username_password_fail.png")
            raise
        else:
            self.login.saveScreeenShot('correct_username_password_pass.png')
            log.info("run completed! please check the test report")

    def test_login_username_incorrect(self):
        """用户名不正确，密码正确，登录失败"""
        self.login.loginFunc(self.login.updowm[1][0],self.login.updowm[1][1])
        time.sleep(2)
        attr_text =  self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text,attr_text)
        log.info("run completed! please check the test report")

    def test_login_failed_incorrect_password(self):
        """用户名正确，密码错误，登录失败"""
        self.login.loginFunc(self.login.updowm[5][0],self.login.updowm[5][1])
        time.sleep(2)
        attr_text = self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text,attr_text)
        log.info("run completed! please check the test report")

    def test_login_failed_username_password_blan(self):
        """用户名为空，密码为空，登录失败"""
        self.login.loginFunc(self.login.updowm[6][0],self.login.updowm[6][1])
        time.sleep(2)
        attr_text = self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text, attr_text)
        log.info("run completed! please check the test report")

    def test_login_failed_username_password_error(self):
        """用户名和密码都错误，登录失败"""
        self.login.loginFunc(self.login.updowm[3][0],self.login.updowm[3][1])
        time.sleep(2)
        attr_text = self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text, attr_text)
        log.info("run completed! please check the test report")

    def test_login_failed_password_blank(self):
        """正确的用户名，空的密码，登录失败"""
        self.login.loginFunc(self.login.updowm[4][0],self.login.updowm[4][1])
        time.sleep(2)
        attr_text = self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text, attr_text)
        log.info("run completed! please check the test report")

    def test_login_failed_username_blank(self):
        """空的用户名，正确的密码，登录失败"""
        self.login.loginFunc(self.login.updowm[2][0],self.login.updowm[2][1])
        time.sleep(2)
        attr_text = self.login.getFailloginText()
        expect_text = "用户名或者密码错误"
        self.login.assertEqual(expect_text, attr_text)
        log.info("run completed! please check the test report")


























if __name__ == "__main__":
    unittest.mian