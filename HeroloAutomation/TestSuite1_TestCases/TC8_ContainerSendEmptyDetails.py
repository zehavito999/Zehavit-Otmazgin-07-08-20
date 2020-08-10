from selenium import webdriver
import unittest
import time


class ContainerEmptyDetails(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_send_empty_details_container(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        send_btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[3]/a")
        send_btn.click()
        time.sleep(3)
        # name label display
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[1]/span/span").is_displayed())
        # company label display
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[1]/div[2]/span/span").is_displayed())
        # email label display
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[1]/span/span").is_displayed())
        # telephone label display
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[1]/form/div[2]/div[2]/span/span").is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()