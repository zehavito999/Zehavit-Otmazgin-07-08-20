from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import selenium
import unittest
import time


class ContainerGetMoreDetails(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_container_validation(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        raised = True
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section")
        except selenium.common.exceptions.NoSuchElementException:
            raised = False
        self.assertTrue(raised)
        # name
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[1]/input").is_displayed())
        # company
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[2]/input").is_displayed())
        # email
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[1]/input").is_displayed())
        # telephone
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[2]/input").is_displayed())
        # button
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[3]/a").is_displayed())
        # contact person image
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[1]/img").is_displayed())
        # contact person
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[1]/div").is_displayed())
        # social media bar
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[2]").is_displayed())

    def tearDown(self):
        self.driver.close()