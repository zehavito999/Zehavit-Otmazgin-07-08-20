import selenium
from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class FooterOneDetailIsMissing(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"
    email="1@gmail.com"
    telephone="0508386875"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_one_missing_detail_footer(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/footer")))
        email=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]/input")
        telephone=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]/input")
        email.send_keys(self.email)
        telephone.send_keys(self.telephone)
        send_btn=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/button")
        send_btn.click()
        raised=False
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]/label/span")#email label not display
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]/label/span")#telephone label not display
        except selenium.common.exceptions.NoSuchElementException:
            raised = True
        self.assertTrue(raised)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[1]/label/span").is_displayed())#name label is display

    def tearDown(self):
        self.driver.close()