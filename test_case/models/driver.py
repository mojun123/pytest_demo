from selenium import webdriver
from test_case.models.RecordLog import log

class WDriver(object):
    def fireFoxDriver(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception as e :
            log.info("FireFoxDriverServer.exe executable needs to be in PATH. Please download!")
            raise e
        else:
            log.info("found the Firefox driver successed")
            return self.driver

    def chromeDriver(self):

        try:
            self.driver = webdriver.Chrome()
        except Exception as e :
            log.info('ChromeDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log.info("found the webdriver driver successed")
            return self.driver

    def ieDriver(self):
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            log.info('IEDriverServer.exe executable needs to be in PATH. Please download!')
            raise e
        else:
            log.info("found the IE driver  successed !")
            return self.driver

if __name__ == '__main__':
    WDrive=WDriver()
    WDrive.chromeDriver()

