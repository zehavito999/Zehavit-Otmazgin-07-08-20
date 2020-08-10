from selenium import webdriver
import unittest
import time


class UIExampleWorks(unittest.TestCase):
    base_url="https://automation.herolo.co.il/"

    def setUp(self):
        self.driver = webdriver.Chrome(r"../Utills/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_example_works_validation(self):
        self.driver.get(self.base_url)
        self.driver.execute_script("window.scrollTo(0,1900)")
        time.sleep(3)
        # title
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/h2/span").is_displayed())
        right_arrow=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[3]/img")
        left_arrow=self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[1]/img")
        self.assertTrue(right_arrow.is_displayed())
        # 1st 4 images
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[2]/div[1]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[2]/div[1]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[2]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[2]/div[2]/div[2]/img").is_displayed())
        right_arrow.click()
        time.sleep(3)
        # 2nd 4 images
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[3]/div[1]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[3]/div[1]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[3]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[3]/div[2]/div[2]/img").is_displayed())
        right_arrow.click()
        time.sleep(3)
        # 3rd 4 images
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[4]/div[1]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[4]/div[1]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[4]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[4]/div[2]/div[2]/img").is_displayed())
        right_arrow.click()
        time.sleep(3)
        # 4th 4 images
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[5]/div[1]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[5]/div[1]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[5]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[5]/div[2]/div[2]/img").is_displayed())
        right_arrow.click()
        time.sleep(3)
        # 5th 4 images
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[6]/div[1]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[6]/div[1]/div[2]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[6]/div[2]/div[1]/img").is_displayed())
        self.assertTrue(self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/div[2]/div/div[6]/div[2]/div[2]/img").is_displayed())
        for click in range(4):
            left_arrow.click()
            time.sleep(1)
        # slicky dots
        self.driver.execute_script("window.scrollTo(0,2000)")
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/ul/li[1]/div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/ul/li[2]/div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/ul/li[3]/div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/ul/li[4]/div").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/section[3]/div/ul/li[5]/div").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()