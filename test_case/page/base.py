from test_case.models.RecordLog import log
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from config import conf




class BasePage(object):
    def __init__(self,driver,url = "http://supplytest.fandow.com"):
        self.driver = driver
        self.base_url = url

    def _open(self,url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.info(e)
            raise ValueError('%s address access error, please check！' %url)

    def open(self):
        self._open(self.base_url)
        log.info('%s loading successed!' %self.base_url)
        return self.base_url

    def find_element(self,by,arg,driver = None,timeout=30):
        driver = driver or self.driver
        try:
            element = WebDriverWait(driver,timeout).until(
                lambda driver:driver.find_element(by,arg)
            )
            return element
        except Exception as e:
            log.info('finding element timeout!, details')


    def find_elements(self,by,arg,driver = None,timeout = 30):
        driver = driver or self.driver
        try:
            element = WebDriverWait(driver, timeout).until(
                lambda driver: driver.find_elements(by, arg)
            )
            return element
        except Exception as e:
            log.info('finding element timeout!, details')

    def find_element_by_id(self, e_id, driver=None, timeout=30):
        return self.find_element(By.ID, e_id, driver, timeout)

    def find_element_by_name(self, e_name, driver=None, timeout=30):
        return self.find_element(By.NAME, e_name, driver, timeout)

    def find_element_by_xpath(self, e_xpath, driver=None, timeout=30):
        return self.find_element(By.XPATH, e_xpath, driver, timeout)

    def find_element_by_link_text(self, e_link_text, driver=None, timeout=30):
        return self.find_element(By.LINK_TEXT, e_link_text, driver, timeout)

    def find_element_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
        return self.find_element(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)

    def find_element_by_tag_name(self, e_tag_name, driver=None, timeout=30):
        return self.find_element(By.TAG_NAME, e_tag_name, driver, timeout)

    def find_element_by_class_name(self, e_class_name, driver=None, timeout=30):
        return self.find_element(By.CLASS_NAME, e_class_name, driver, timeout)

    def find_element_by_css_selector(self, e_css_selector, driver=None, timeout=30):
        return self.find_element(By.CSS_SELECTOR, e_css_selector, driver, timeout)

    def find_elements_by_name(self, e_name, driver=None, timeout=30):
        return self.find_elements(By.NAME, e_name, driver, timeout)

    def find_elements_by_xpath(self, e_xpath, driver=None, timeout=30):
        return self.find_elements(By.XPATH, e_xpath, driver, timeout)

    def find_elements_by_link_text(self, e_link_text, driver=None, timeout=30):
        return self.find_elements(By.LINK_TEXT, e_link_text, driver, timeout)

    def find_elements_by_partial_link_text(self, e_partial_link_text, driver=None, timeout=30):
        return self.find_elements(By.PARTIAL_LINK_TEXT, e_partial_link_text, driver, timeout)

    def find_elements_by_tag_name(self, e_tag_name, driver=None, timeout=30):
        return self.find_elements(By.TAG_NAME, e_tag_name, driver, timeout)

    def find_elements_by_class_name(self, e_class_name, driver=None, timeout=30):
        return self.find_elements(By.CLASS_NAME, e_class_name, driver, timeout)

    def find_elements_by_css_selector(self, e_css_selector, driver=None, timeout=30):
        return self.find_elements(By.CSS_SELECTOR, e_css_selector, driver, timeout)

    def inputValue(self,element,value):
        """
        :param element: element参数是要页面元素的
        :param value:
        :return:
        """
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            log.info('typing value error!')
            raise e
        else:
            log.info('inputValue:[%s] is receiveing value [%s]' % (element, value))

    #获取元素数据
    def getValue(self,element):
        try:
            value = element.text
        except Exception:
            value = element.get_attribute("value")
            log.info('reading the element [%s] value [%s]' % (element, value))
            return value
        except:
            log.logger.exception('read value failed')
            raise Exception
        else:
            log.logger.info('reading the element [%s] value [%s]' % (element, value))
            return value

    def getValues(self,elements):
        value_list = []
        try:
            for element in elements:
                value = elements.text
                value_list.append(value)
        except Exception as e:
            log.info('read value failed')
            raise e
        else:
            return value_list

    #判断元素是否存在
    def visibility_of_element_located(self, by, arg, driver=None, visibiliy=True, timeout=30):
        '''
        An expectation for checking that an element is present on the DOM of a page and visible.
        Visibility means that the element is not only displayed but also has a height and width that is greater than 0.
        locator - used to find the element returns the WebElement once it is located and visible
        @param
            (by, arg) -- locator
            locator is tuple, as follow:
                (By.CLASS_NAME, class name)
                (By.CSS_SELECTOR, css selector)
                (By.ID, id)
                (By.LINK_TEXT, link text)
                (By.NAME, name)
                (By.PARTIAL_LINK_TEXT, partial link text)
                (By.TAG_NAME, tag name)
                (By.XPATH, xpath)
        '''
        driver = driver or self.driver
        element = None
        try:
            if visibiliy:
                element = WebDriverWait(driver, timeout).until(
                    EC.visibility_of_element_located((by, arg)))
            else:
                element = WebDriverWait(driver, timeout).until(
                    EC.invisibility_of_element_located((by, arg)))
            return element

        except Exception as e:
            # print("wait_for_element timeout: ")
            print(str(e))
            return None


    #截图
    def saveScreeenShot(self,filename):
        """

        :param filename:
        :return:
        """
        list_value = []
        list = filename.split('.')
        for value in list:
            list_value.append(value)
        if list_value[1] == 'png' or list_value[1] =='jpg' or list_value[1] == "PNG" or list_value[1]=="JPG":
            if "fail" in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(conf.failImagePath,filename))
                except Exception:
                    log.info("save screenshot failed")
                else:
                    log.info('the file [%s]  save screenshot successed under [%s]' % (filename, conf.failImagePath))
            elif 'pass' in list_value[0]:
                try:
                    self.driver.save_screenshot(os.path.join(conf.pasImagePath,filename))
                except Exception:
                    log.info("save screenshot failed")
                else:
                    log.info( 'the file [%s]  save screenshot successed under [%s]' % (filename, conf.passImagePath))
            else:
                log.info('save screenshot failed due to [%s] format incorrect' %filename)
        else:
            log.info('the file name of [%s] format incorrect cause save screenshot failed, please check!' % filename)


    def delete_all_cookies(self):
        self.driver.delete_all_cookies()





