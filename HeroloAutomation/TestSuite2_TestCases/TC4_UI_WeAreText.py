from selenium import webdriver
import unittest
import time


class UIWeAreText(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_we_are_text_validation(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/h2[1]/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/div").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/div/h1[1]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/div/h4[1]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[1]/div/h4[2]").is_displayed())

    def tearDown(self):
        self.driver.close()