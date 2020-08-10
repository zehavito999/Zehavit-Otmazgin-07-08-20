from selenium import webdriver
import unittest
import time


class UICompanyCustomers(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_company_works_validation(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0,2700)")
        time.sleep(3)
        # title
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[4]/div[2]/h2/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[4]/div[2]/h2/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[4]/div[2]/div/div/div").is_displayed())

    def tearDown(self):
        self.driver.close()