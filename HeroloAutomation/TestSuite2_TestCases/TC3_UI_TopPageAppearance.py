from selenium import webdriver
import unittest
import time


class UITopPageAppearance(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_top_page_validation(self):
        self.driver.get(self.base_url)
        time.sleep(3)
        # logo
        self.assertTrue(self.driver.find_element_by_id("logom").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/section/div[2]/h2[1]/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/section/div[2]/h2[2]/span").is_displayed())
        # vue icon
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/div/img[3]").is_displayed())
        # react icon
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/div/img[2]").is_displayed())
        # angular icon
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/header/div/img[1]").is_displayed())

    def tearDown(self):
        self.driver.close()