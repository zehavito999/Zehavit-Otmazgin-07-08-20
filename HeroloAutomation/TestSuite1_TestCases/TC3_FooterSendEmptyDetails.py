from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import selenium
import unittest
import time


class FooterEmptyDetails(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_send_empty_details_footer(self):
        self.driver.get(self.base_url)
        time.sleep(5)
        # footer
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer").is_displayed())
        send_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/button")
        send_btn.click()
        time.sleep(3)
        # missing name label
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[1]/label/span").is_displayed())
        # missing email label
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[2]/label/span").is_displayed())
        # missing telephone label
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer/form/div/div[3]/label/span").is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()


