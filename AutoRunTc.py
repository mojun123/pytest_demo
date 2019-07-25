from test_case.models.testreport import *
from test_case.LoginTc import Login_TC



class RunTcScript(object):
    """

    """
    def __init__(self):
        self.suite = unittest.TestSuite()

    #
    def load_login_tc(self,testcase):
        """

        :param testcase:
        :return:
        """
        self.suite.addTest(Login_TC(testcase))




