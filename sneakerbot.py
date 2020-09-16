from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException


def get_product_url():
    print("Insert product url:\n")
    product_url = input()
    return product_url


def get_size():
    size_chart = {
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
    print("Select size\n")
    for key in size_chart:
        print(key + "   " + size_chart[key])
    key = input()
    size = str(size_chart[key])
    return size_chart, size


def get_login_info():
    print("Enter username")
    username = input()

    print("Enter password")
    user_password = input()
    return username, user_password


def get_driver():
    """options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)"""
    driver = webdriver.Chrome()
    return driver


def get_nike_site(product_url, driver):
    driver.get(product_url)
    driver.refresh()


def find_size(driver, size):
    button = driver.find_element_by_xpath('//button[text()="'+size+'"]')
    button.click()
    driver.implicitly_wait(10)


def add_to_cart(driver):
    add_to_cart_button = driver.find_element_by_xpath('//button[text()="Add to Cart"]')
    add_to_cart_button.click()


def checkout(driver):
    checkout_button = driver.find_element_by_xpath('//button[text()="Checkout"]')
    checkout_button.click()


def login(driver, username, user_password):
    """join = driver.find_element_by_xpath('//button[text()="Join / Log In"]')
    join.click()"""

    email = driver.find_element_by_name("emailAddress")
    password = driver.find_element_by_name("password")

    email.send_keys(username)
    password.send_keys(user_password)

    """sign_in = driver.find_element_by_xpath('//input[@value="SIGN IN"]')
    sign_in.click()"""

    login_button = driver.find_element_by_xpath('//input[@value="MEMBER CHECKOUT"]')
    login_button.click()


def place_order(driver):
    cvv = driver.find_element_by_id("cvNumber")
    cvv.send_keys("CVV NUMBER")

    place_order_button = driver.find_element_by_xpath('//input[@value="Buy"')
    place_order_button.click()

    driver.save_screenshot("order_confirmation.png")


def driver_quit(driver):
    driver.quit()


def main():
    product_url = get_product_url()
    size_chart, size = get_size()
    username, user_password = get_login_info()
    driver = get_driver()
    time.sleep(5)

    try:
        if driver:
            get_nike_site(product_url, driver)
    except:
        print("Could not go to given URL, check if URL was correct, sys exit")
        sys.exit()

    try:
        find_size(driver, size)#2
    except NoSuchElementException:
        print("Size not available")
        sys.exit()

    try:
        add_to_cart(driver)#3
    except NoSuchElementException:
        print("Product sold out")
        sys.exit()

    try :
        checkout(driver)
    except NoSuchElementException:
        print("Problem with checkout")
        sys.exit()

    try:
        login(driver, username, user_password)#1
    except NoSuchElementException:
        print("Invalid login information")
        sys.exit()

    try:
        place_order(driver)#4
    except NoSuchElementException:
        print("Problem with payment method")
        sys.exit()

    driver_quit(driver)


if __name__ == "__main__":
    main()
