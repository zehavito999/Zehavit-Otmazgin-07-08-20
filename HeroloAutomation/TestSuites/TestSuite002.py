import unittest
from Utills import UtillsFunctions
from HtmlTestRunner import HTMLTestRunner

test_suite002 = UtillsFunctions.init_test_suite("2")
loader = unittest.TestLoader()

results= HTMLTestRunner(combine_reports=True, report_name="TestSuite002", add_timestamp=False,output=r'../Reports').run(test_suite002)

