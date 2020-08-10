import unittest
from Utills import UtillsFunctions
from HtmlTestRunner import HTMLTestRunner

test_suite001 = UtillsFunctions.init_test_suite("1")
loader = unittest.TestLoader()

results= HTMLTestRunner(combine_reports=True, report_name="TestSuite001", add_timestamp=False,output=r'../Reports').run(test_suite001)



