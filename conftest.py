from selenium import webdriver
import pytest
from Login_auth import login_auth

@pytest.fixture
def browser_open():
    browser = webdriver.Chrome()
    browser.get("https://www.selenium.dev/selenium/web/web-form.html")
    yield browser
    browser.quit()


