import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.saucedemo.com"
userr = "standard_user"
passwd = "secret_sauce"


@pytest.fixture
def driver():
    driver = webdriver.Safari()
    yield driver
    driver.quit()


def test_login_success_simple(driver):
    driver.get(url)
    time.sleep(1)
    user = driver.find_element(By.ID, "user-name")
    pwd = driver.find_element(By.NAME, "password")
    btn = driver.find_element(By.ID, "login-button")

    user.clear()
    user.send_keys(userr)
    pwd.clear()
    pwd.send_keys(passwd)
    btn.click()

    time.sleep(5)
    assert "/inventory.html" in driver.current_url or len(driver.find_elements(By.ID, "inventory_container")) > 0
