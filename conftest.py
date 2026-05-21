from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from Login_auth import login_auth
import os
from Logout_auth import logout_auth


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
    
@pytest.fixture(scope="session")
def login(browser:WebDriver):
    browser_login = login_auth(browser)
    browser.get("https://www.saucedemo.com/")

    if os.path.exists("cookies.pkl"):
        try:
            browser_login.load_cookie()
            if "inventory.html" not in browser.current_url:
                browser_login.login()
                browser_login.save_cookie()
        except Exception:
            os.remove("cookies.pkl")
            browser_login.login()
            browser_login.save_cookie()
    else:
        browser_login.login()
        browser_login.save_cookie()
         
         
    yield browser
     
@pytest.fixture(scope="session")    
def logout(browser:WebDriver):
    browser_logout=logout_auth(browser)
    browser_logout.logout()
    
    
    
    
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