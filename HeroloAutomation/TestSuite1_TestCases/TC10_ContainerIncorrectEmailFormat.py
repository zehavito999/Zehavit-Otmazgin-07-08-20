from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import selenium
import unittest
import time


class ContainerIncorrectEmailFormat(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"
    name = "zehavit"
    company = "herolo"
    email = "1gmail.com"
    telephone = "0508386875"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_insert_incorrect_email_format(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        name = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[1]/input")
        company = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[2]/input")
        email = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[1]/input")
        telephone = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[2]/input")
        name.send_keys(self.name)
        company.send_keys(self.company)
        email.send_keys(self.email)
        telephone.send_keys(self.telephone)
        time.sleep(3)
        send_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[3]/a")
        send_btn.click()
        raised=False
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[1]/span/span")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[1]/span/span")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[2]/span/span")
            self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[1]/span/span").is_displayed())
        except selenium.common.exceptions.NoSuchElementException:
            raised = True
        self.assertTrue(raised)

    def tearDown(self):
        self.driver.close()