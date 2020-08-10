import unittest
import os
from importlib import import_module

def init_test_suite(i):
    loader = unittest.TestLoader()
    modules_to_test=[]
    modules_to_import=[]
    # path="../TestSuite2_TestCases"
    path = "../TestSuite" + i + "_TestCases"
    test_dir=os.listdir(path)
    for test in test_dir:
        if test.startswith("TC") and test.endswith(".py"):
            modules_to_import.append("TestSuite" + i + "_TestCases." + test.rstrip('.py'))
            modules_to_test.append(test.rstrip('.py'))
    all_tests=unittest.TestSuite()
    for module in (modules_to_import):
        test_module = import_module(module)
        all_tests.addTest(loader.loadTestsFromModule(test_module))
    return all_tests