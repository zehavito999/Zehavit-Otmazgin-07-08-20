from selenium import webdriver
import unittest
import time


class UIWhatsApp(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_whatsapp_icon_validation(self):
        self.driver.get(self.base_url)
        parent_browser = self.driver.current_window_handle
        whatsapp_icon = self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/a[2]")
        self.assertTrue(whatsapp_icon.is_displayed())
        whatsapp_icon.click()
        self.driver.switch_to.window(parent_browser)
        self.driver.execute_script("window.scrollTo(0,500)")
        whatsapp_icon.click()
        self.driver.switch_to.window(parent_browser)
        time.sleep(3)
        self.assertTrue(whatsapp_icon.is_displayed())
        self.driver.execute_script("window.scrollTo(0,4000)")
        whatsapp_icon.click()
        self.driver.switch_to.window(parent_browser)
        time.sleep(3)
        self.assertTrue(whatsapp_icon.is_displayed())
        self.driver.execute_script("window.scrollTo(0,5500)")
        whatsapp_icon.click()
        self.driver.switch_to.window(parent_browser)
        time.sleep(3)
        self.assertTrue(whatsapp_icon.is_displayed())

    def tearDown(self):
        self.driver.close()