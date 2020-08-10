from selenium import webdriver
import unittest
import time


class UIQuestions(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_questions_validation(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0,3300)")
        time.sleep(3)
        # title
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/h2/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[1]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[1]/p/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[2]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[2]/p/span").is_displayed())
        self.driver.execute_script("window.scrollTo(0,3600)")
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[3]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[3]/p/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[4]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[4]/p/span").is_displayed())
        self.driver.execute_script("window.scrollTo(0,3700)")
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[5]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[5]/p/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[6]/h4/span").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[5]/div/section[6]/p/span").is_displayed())

    def tearDown(self):
        self.driver.close()