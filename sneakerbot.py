from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def set_up():
    driver = webdriver.Chrome()
    return driver


def test_search_in_nike(driver):
    driver.get("https://www.nike.com/launch")

    in_stock_button = driver.find_element_by_xpath("//div[text()='In Stock']")
    in_stock_button.click()

    driver.implicitly_wait(10)

    product_id_button = driver.find_element_by_xpath('//img[contains(@alt, "Air Zoom-Type \'Hyper Pink\'")]')
    product_id_button.click()

    button = driver.find_element_by_xpath('//button[text()="M 10 / W 11.5"]')
    button.click()

    add_to_cart_button = driver.find_element_by_xpath('//button[text()="Add to Cart"]')
    add_to_cart_button.click()

    checkout_button = driver.find_element_by_xpath('//button[text()="Checkout"]')
    checkout_button.click()

    email = driver.find_element_by_name("emailAddress")
    password = driver.find_element_by_name("password")

    email.send_keys("email address")
    password.send_keys("password")

    login_button = driver.find_element_by_xpath('//input[@value="MEMBER CHECKOUT"]')
    login_button.click()

    #cvv = driver.find_element_by_id("cvNumber")
    #cvv.send_keys("CVV NUMBER")

    #place_order_button = driver.find_element_by_xpath('//input[@value="Place Order"')
    #place_order_button.click()


def driver_quit(driver):
    driver.quit()


def main():
    driver = set_up()
    test_search_in_nike(driver)
    driver_quit(driver)


if __name__ == "__main__":
    main()
