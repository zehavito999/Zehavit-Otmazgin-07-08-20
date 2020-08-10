from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class FooterGetMoreDetailsDisappear(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_footer_disappear(self):
        self.driver.get(self.base_url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div/footer")))
        footer = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/footer")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        self.assertFalse(footer.is_displayed())
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section") #container
        self.assertTrue(self.driver.find_element_by_id("name").is_displayed())
        self.assertTrue(self.driver.find_element_by_id("company").is_displayed())
        self.assertTrue(self.driver.find_element_by_id("email").is_displayed())
        self.assertTrue(self.driver.find_element_by_id("telephone").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[1]/img").is_displayed())#contact person image
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[1]/div").is_displayed())#contact person
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[6]/section/div[2]/div/div[2]").is_displayed())#social media bar

    def tearDown(self):
        self.driver.close()