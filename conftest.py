from selenium import webdriver
import pytest
from Login_auth import login_auth


def base_url():
    return "https://www.saucedemo.com/"


@pytest.fixture
def login():
    browser_login = login_auth()
    browser_login.login()
    browser_login.save_cookie()
    browser_login.load_cookie()


@pytest.fixture
def browser_open(base_url,login):
    browser = webdriver.Chrome()
    base_url()
    login()
    yield browser
    browser.quit()
'''
@pytest.fixture(scope="session", autouse=True)
def login(browser):
    auth = login_auth(browser)
    auth.login()
    return browser

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


'''