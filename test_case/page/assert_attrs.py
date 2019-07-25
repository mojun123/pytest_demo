from test_case.page.base import BasePage



class AssertAttrs(BasePage):
    def assertEqual(self,expected_attr, real_attr,msg = ""):
        if not msg:
            msg = msg = " Expected attribute: {}, but got real attribute: {}".format(expected_attr, real_attr)
        try:
            assert expected_attr == real_attr,msg
        except Exception as e:
            raise e

    def assertNotEqual(self,expected_attr,real_attr,msg=""):
        if not msg:
            msg = msg = " Expected attribute: {} do compare equal to real attribute: {}".format(expected_attr, real_attr)
        try :
            assert expected_attr != real_attr, msg
        except Exception as e:
            return e

    def assertTrue(self, expected_attr, msg=''):
        if not msg:
            msg = " Expected attribute: True, but got real attribute: {}".format(expected_attr)
        try:
            assert expected_attr is True, msg
        except Exception as e:
            raise e


    def assertFalse(self, expected_attr, msg=''):
        if not msg:
            msg = " Expected attribute: False, but got real attribute: {}".format(expected_attr)
        try:
            assert expected_attr is False, msg
        except Exception as e:
            raise e


    def assertIs(self, expected_attr, real_attr, msg=''):
        if not msg:
            msg = " Expected attribute: {}, but real attribute: {}".format(expected_attr, real_attr)
        try:
            assert expected_attr is real_attr, msg
        except Exception as e:
            raise e


    def assertIsNot(self, expected_attr, real_attr, msg=''):
        if not msg:
            msg = " Expected attribute: {} as the same as real attribute: {}".format(expected_attr, real_attr)
        try:
            assert expected_attr is not real_attr, msg
        except Exception as e:
            raise e


    def assertIsNone(self, expected_attr, msg=''):
        if not msg:
            msg = " Expected attribute shoule be: None. But got real attribute: {}".format(expected_attr)
        try:
            assert expected_attr is None, msg
        except Exception as e:
            raise e


    def assertIsNotNone(self, expected_attr, msg=''):
        if not msg:
            msg = " Expected attribute shoule be not: None. But got real attribute: {}".format(expected_attr)
        try:
            assert expected_attr is not None, msg
        except Exception as e:
            raise e


    def assertIn(self, expected_attr, real_attr, msg=''):
        if not msg:
            msg = " Expected attribute: {} not in the real attribute: {}".format(expected_attr, real_attr)
        try:
            assert expected_attr in real_attr, msg
        except Exception as e:
            raise e


    def assertNotIn(self, expected_attr, real_attr, msg=''):
        if not msg:
            msg = " Expected attribute: {} in the real attribute: {}".format(expected_attr, real_attr)
        try:
            assert expected_attr not in real_attr, msg
        except Exception as e:
            raise e


    def assertInOrNotIn(self, expected_attr, real_attr, msg='', reverse=False):
        if not reverse:
            self.assertIn(expected_attr, real_attr, msg)
        else:
            self.assertNotIn(expected_attr, real_attr, msg)


    def assertEqOrNotEqual(self, expected_attr, real_attr, msg='', reverse=False):
        if not reverse:
            self.assertEqual(expected_attr, real_attr, msg)
        else:
            self.assertNotEqual(expected_attr, real_attr, msg)


    def assert_text_by_lower(self, expected_attr, element, msg=''):
        try:
            real_attr = element.text
            real_attr = real_attr.lower()
            if not msg:
                msg = " Expected attribute: {} in the real attribute: {}".format(expected_attr, real_attr)
            assert expected_attr in real_attr, msg
        except Exception as e:
            raise e

    def assert_greater_equal(self, expected_attr, real_attr, msg=''):
        if not msg:
            msg = " Expected attribute: {} in the real attribute: {}".format(expected_attr, real_attr)

        try:
            assert expected_attr >= real_attr, msg
        except Exception as e:
            raise e


