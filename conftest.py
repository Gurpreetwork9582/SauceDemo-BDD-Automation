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





