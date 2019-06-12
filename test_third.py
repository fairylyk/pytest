# import unittest


def div(a, b):
    return a - b


class Test(object):

    def test_div_001(self):
        assert div(2, 1) == 1

    # def test_div_002(self):
    #     self.assertEqual(div(3, 54), 5)
    #
    # def test_div_003(self):
    #     self.assertEqual(div(4, 2), 18)
