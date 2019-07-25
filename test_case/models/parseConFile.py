import configparser
from config.conf import configDir

class ParseConFile(object):
    def __init__(self):
        self.file = configDir
        self.conf = configparser.ConfigParser()
        self.conf.read(self.file,encoding="utf-8")

    def getAllSections(self):
        """获取所有的section，返回一个列表"""
        return self.conf.sections()

    def getAllOptions(self,section):
        """获取指定section下所有的option，返回列表"""
        return self.getAllOptions(section)

    def getLocatorsOrAccount(self,section,option):
        """获取指定section, 指定option对应的数据, 返回元祖和字符串"""
        try :
            locator = self.conf.get(section,option)
            if ("->" in locator):
                locator = tuple(locator.split("->"))
                return locator[1]
        except configparser.NoOptionError as e:
            print("error",e)

        return 'error: No option "{}" in section: "{}"'.format(option, section)

    def getOptionValue(self,section):
        """获取指定section下所有的option和对应的数据，返回字典"""
        value = dict(self.conf.items(section))
        return value

if __name__ == "__main__":
    cfg = ParseConFile()
    value = cfg.getAllSections()
    element = cfg.getLocatorsOrAccount("LoginPageElements","username")
    print(value)
    print(element)