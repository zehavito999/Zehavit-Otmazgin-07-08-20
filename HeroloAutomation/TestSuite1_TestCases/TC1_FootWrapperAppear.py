from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FooterGetMoreDetails(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_footer_elements_validation(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/footer")))
        footer = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer")
        # footer
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer").is_displayed())
        # how can we help label
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/label").is_displayed())
        # name input
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[1]/input").is_displayed())
        # email input
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]").is_displayed())
        # telephone input
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]").is_displayed())
        # button
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/button").is_displayed())
        self.driver.execute_script("window.scrollTo(0,200)")
        self.assertTrue(footer.is_displayed())
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,2000)")
        self.assertTrue(footer.is_displayed())
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,4000)")
        self.assertTrue(footer.is_displayed())
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,5500)")
        self.assertFalse(footer.is_displayed())

    def tearDown(self):
        self.driver.close()