import unittest
#import java.util.concurrent.TimeUnit;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NikeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_nike(self):
        driver = self.driver
        driver.get("https://www.nike.com/launch")

        button = driver.find_element_by_xpath('//button[text()="Join / Log In"]')
        button.click()

        email = driver.find_element_by_name("emailAddress")
        password = driver.find_element_by_name("password")

        email.send_keys("maki.dominic@yahoo.com")
        password.send_keys("Yeabuddy1234")

        login_button = driver.find_element_by_xpath('//input[@value="SIGN IN"]')
        login_button.click()

        try:
            element = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, "myDynamicElement"))
            )
        finally:
            driver.quit()
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
