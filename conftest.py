from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from Login_auth import login_auth
import os


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
    
@pytest.fixture(scope="session")
def login(browser:WebDriver):
    browser_login = login_auth(browser)
    if os.path.exists("cookies.pkl"):
        try:
            browser_login.load_cookie()
        except Exception:
            # If cookie loading fails, delete and perform login
            os.remove("cookies.pkl")
            browser_login.login()
            browser_login.save_cookie()
    else:
        browser_login.login()
        browser_login.save_cookie()
         
         
    yield browser
     
    
    
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