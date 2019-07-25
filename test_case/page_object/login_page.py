from test_case.page.assert_attrs import AssertAttrs
from selenium import webdriver
from test_case.models.parseConFile import ParseConFile
from test_case.models.RecordLog import log
import sys
from test_case.models.parseExcelFile import ParseExcel
class LoginPage(AssertAttrs):
    """用户名，密码，登录按钮，错误提示的页面元素"""
    cfp = ParseConFile()
    username = cfp.getLocatorsOrAccount('LoginPageElements', 'username')
    password = cfp.getLocatorsOrAccount('LoginPageElements', 'password')
    loginBtn = cfp.getLocatorsOrAccount('LoginPageElements', 'loginBtn')
    accountNull = cfp.getLocatorsOrAccount("LoginPageElements","accountNull")
    passwordNull = cfp.getLocatorsOrAccount("LoginPageElements","passwordNull")
    errMessage = cfp.getLocatorsOrAccount("LoginPageElements","errMessage")

    pe = ParseExcel()
    sheet = pe.getSheetByName("login")
    #用户名和密码
    updowm = pe.getAllValueOfSheet(sheet)


    #登录按钮
    def clickLogBtn(self):
        """

        :return:
        """
        element = self.find_element_by_xpath(self.loginBtn)
        element.click()
        log.info("loginning...")

    # 密码为空
    def getFailpassText(self):
        info = self.find_element_by_xpath(self.passwordNull).text
        log.info("login failed")
        return info


    #账号为空
    def getFailaccountText(self):
        info = self.find_element_by_xpath(self.accountNull).text
        log.info("login failed")
        return info

    #账号名或者密码错误

    def getFailloginText(self):
        info = self.find_element_by_xpath(self.errMessage).text
        log.info("login fail")
        return info

    #统一登录函数

    def loginFunc(self,username = "fd-0001",password= "123456"):
        """

        :param username:
        :param password:
        :return:
        """
        elementName = self.find_element_by_xpath(self.username)
        elementPass = self.find_element_by_xpath(self.password)
        self.inputValue(elementName,username)
        self.inputValue(elementPass,password)
        self.clickLogBtn()


