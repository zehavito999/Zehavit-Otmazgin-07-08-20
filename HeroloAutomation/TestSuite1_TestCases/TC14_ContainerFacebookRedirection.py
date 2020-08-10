from selenium import webdriver
import unittest
import time


class ContainerRedirectionFacebook(unittest.TestCase):
    base_url = "https://automation.herolo.co.il/"


    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_redirect_to_facebook(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        # redirection
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[2]/div/a[3]").click()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()