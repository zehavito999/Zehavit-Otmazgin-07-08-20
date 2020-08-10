from selenium import webdriver
import unittest
import time


class UIPopUpContactus(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"
    name = "zehavit"
    email = "1@gmail.com"
    telephone = "0501112234"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_pop_up_contact_us(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0,500)")
        time.sleep(30)
        pop_up = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div")
        pop_up.is_displayed()
        name = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div/div[1]/input")
        email = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div/div[2]/input")
        telephone = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/div/div[3]/input")
        send_btn = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[2]/form/button")
        name.send_keys(self.name)
        email.send_keys(self.email)
        telephone.send_keys(self.telephone)
        send_btn.click()
        # wait until redirect to thank you page
        time.sleep(8)
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div/div[1]/div/main/div[1]/div[2]/div[1]/a/button").is_displayed())

    def tearDown(self):
        self.driver.close()
