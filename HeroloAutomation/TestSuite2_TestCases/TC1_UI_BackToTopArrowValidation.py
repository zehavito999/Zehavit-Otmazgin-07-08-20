from selenium import webdriver
import unittest
import time


class UIBackToTopArrow(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_back_to_top_arrow_validation(self):
        self.driver.get(self.base_url)
        back_to_top_arrow = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/a[1]")
        self.assertFalse(back_to_top_arrow.is_displayed())
        self.driver.execute_script("window.scrollTo(0,3000)")
        time.sleep(3)
        self.assertTrue(back_to_top_arrow.is_displayed())
        back_to_top_arrow.click()
        time.sleep(3)
        self.assertFalse(back_to_top_arrow.is_displayed())
        self.driver.execute_script("window.scrollTo(0,5000)")
        time.sleep(3)
        self.assertTrue(back_to_top_arrow.is_displayed())
        back_to_top_arrow.click()
        time.sleep(3)
        self.assertFalse(back_to_top_arrow.is_displayed())
        self.driver.execute_script("window.scrollTo(0,0)")
        time.sleep(3)
        self.assertFalse(back_to_top_arrow.is_displayed())

    def tearDown(self):
        self.driver.close()
