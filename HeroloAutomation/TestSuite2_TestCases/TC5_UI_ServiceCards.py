from selenium import webdriver
import unittest
import time


class UIServiceCards(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_service_cards_validation(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0,1000)")
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]").is_displayed())
        # how can we help label
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/h2").is_displayed())
        #service cards container
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]").is_displayed())
        # right card
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[1]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[1]/div").is_displayed())
        # middle card
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[2]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[2]/div").is_displayed())
        # left card
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[3]").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[3]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[2]/div[2]/div[3]/div").is_displayed())

    def tearDown(self):
        self.driver.close()