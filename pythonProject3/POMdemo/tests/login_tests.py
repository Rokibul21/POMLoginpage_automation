
import pytest
import time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

from POMdemo.tests.pages.login_page_test import LoginPage


@pytest.fixture()
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://ebs.esquire.com.bd/")
    time.sleep(1)
    login_page.enter_username("EC00007439")
    login_page.enter_password("hasan@123")
    time.sleep(1)
    login_page.login_button_click()
    time.sleep(1)
