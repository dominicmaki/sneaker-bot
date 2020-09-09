from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_dict():
    d = {
        "1": "M 5 / W 6.5",
        "2": "M 5.5 / W 7",
        "3": "M 6 / W 7.5",
        "4": "M 6.5 / W 8",
        "5": "M 7 / W 8.5",
        "6": "M 7.5 / W 9",
        "7": "M 8 / W 9.5",
        "8": "M 8.5 / W 10",
        "9": "M 9 / W 10.5",
        "10": "M 9.5 / W 11",
        "11": "M 10 / W 11.5",
        "12": "M 10.5 / W 12",
        "13": "M 11 / W 12.5",
        "14": "M 11.5 / W 13",
        "15": "M 12 / W 13.5",
        "16": "M 12.5 / W 14",
        "17": "M 13 / W 14.5",
        "18": "M 14 / W 15.5",
        "19": "M 15 / W 16.5"
    }
    return d


def set_up(product_url):
    """options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)"""
    driver = webdriver.Chrome()
    driver.get(product_url)
    return driver


def get_size(driver, size):
    button = driver.find_element_by_xpath('//button[text()="' + size + '"]')
    button.click()
    driver.implicitly_wait(10)


def add_to_cart(driver):
    add_to_cart_button = driver.find_element_by_xpath('//button[text()="Buy"]')
    add_to_cart_button.click()


def checkout(driver):
    checkout_button = driver.find_element_by_xpath('//button[text()="Checkout"]')
    checkout_button.click()


def login(driver):
    join = driver.find_element_by_xpath('//button[text()="Join / Log In"]')
    join.click()

    email = driver.find_element_by_name("emailAddress")
    password = driver.find_element_by_name("password")

    email.send_keys(username)
    password.send_keys(user_password)

    sign_in = driver.find_element_by_xpath('//input[@value="SIGN IN"]')
    sign_in.click()


def place_order(driver):
    cvv = driver.find_element_by_id("cvNumber")
    cvv.send_keys("CVV NUMBER")

    place_order_button = driver.find_element_by_xpath('//input[@value="Buy"')
    place_order_button.click()

    driver.save_screenshot("order_confirmation.png")


def driver_quit(driver):
    driver.quit()


def main():
    print("Insert product url:\n")
    product_url = input()

    d = get_dict()
    print("Select size\n")
    for key in d:
        print(key + "   " + d[key])
    key = input()
    size = str(d[key])

    #   time.sleep(5)

    driver = set_up(product_url)
    get_size(driver, size)
    add_to_cart(driver)
    checkout(driver)
    login(driver)
    place_order(driver)

    driver_quit(driver)


if __name__ == "__main__":
    main()
