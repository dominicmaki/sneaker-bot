import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NikeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_nike(self):
        # path = "C:\Users\Dom\PycharmProjects\sneaker_bot"
        driver = self.driver
        driver.get("https://www.nike.com/launch")
        #   self.assertIn("", driver.title)
        print(driver.title)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
