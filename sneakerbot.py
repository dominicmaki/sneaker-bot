from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def set_up():
    driver = webdriver.Chrome()
    return driver


def test_search_in_nike(driver):
    driver.get("https://www.nike.com/launch")

    """button = driver.find_element_by_xpath('//button[text()="Join / Log In"]')
    button.click()

    login_button = driver.find_element_by_xpath('//input[@value="SIGN IN"]')
    login_button.click()"""

    in_stock_button = driver.find_element_by_xpath("//div[text()='In Stock']")
    in_stock_button.click()

    product_id_button = driver.find_element_by_xpath('//img[contains(@alt, "Air Zoom-Type \'Hyper Pink\'")]')
    product_id_button.click()
    #wait or something this should work

    button = driver.find_element_by_xpath('//button[text()="M 10 / W 11.5"]')
    button.click()

    add_to_cart_button = driver.find_element_by_xpath('//button[text()="ADD TO CART"]')
    add_to_cart_button.click()

    checkout_button = driver.find_element_by_xpath('//button[text()="Checkout"]')
    checkout_button.click()

    email = driver.find_element_by_name("emailAddress")
    password = driver.find_element_by_name("password")

    email.send_keys("maki.dominic@yahoo.com")
    password.send_keys("Yeabuddy1234")

    login_button = driver.find_element_by_xpath('//input[@value="MEMBER CHECKOUT"]')
    login_button.click()

    try:
        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "myDynamicElement"))
        )
    finally:
        driver.quit()


def main():
    driver = set_up()
    test_search_in_nike(driver)


if __name__ == "__main__":
    main()
