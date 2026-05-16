from selenium import webdriver
import pytest
from Login_auth import login_auth


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    
    
@pytest.fixture(scope="session")
def login(browser):
    browser_login = login_auth(browser)
    browser_login.login()
    browser_login.save_cookie()
    browser_login.load_cookie()   
    
    
    
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