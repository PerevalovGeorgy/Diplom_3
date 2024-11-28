import pytest
from data import TestUrl, UserData, DRIVER_NAME
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        DRIVER_NAME = "chrome"
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
    else:
        DRIVER_NAME = "firefox"
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
    driver.quit()

@pytest.fixture
def driver_login(driver):
    driver.get(TestUrl.URL_LOGIN_PAGE)
    login_page = LoginPage(driver)
    login_page.add_email_user()
    login_page.add_password_user()
    login_page.click_on_enter_button()
    yield driver
    driver.quit()

