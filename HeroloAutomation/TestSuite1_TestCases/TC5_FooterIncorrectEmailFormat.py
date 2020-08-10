from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest


class FooterIncorrectEmailFormat(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"
    email = "1gmail.com"
    telephone = "0508386875"
    name = "zehavit"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_insert_incorrect_email_format(self):
        self.driver.get(self.base_url)
        name = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[1]/input")
        email = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]/input")
        telephone = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]/input")
        email.send_keys(self.email)
        telephone.send_keys(self.telephone)
        name.send_keys(self.name)
        send_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/button")
        send_btn.click()
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]/label/span").is_displayed())
        raised = False
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[1]/label/span")
            self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]/label/span")
        except NoSuchElementException:
            raised = True
        self.assertTrue(raised)

    def tearDown(self):
        self.driver.close()